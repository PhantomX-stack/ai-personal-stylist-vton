"""FastAPI application for AI Personal Stylist & Virtual Try-On system."""
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from services import recommendation_engine, virtual_tryon, chatbot
from services.vision.vision_pipeline import vision_pipeline
import numpy as np
import cv2
from core.schemas import (
    AnalysisResult,
    OutfitRecommendationRequest,
    OutfitRecommendationResponse,
    ChatRequest,
)
import os

# Initialize FastAPI app
app = FastAPI(
    title="AI Personal Stylist & Virtual Try-On",
    description="Modular AI system for outfit recommendations and virtual clothing try-on",
    version="1.0.0"
)

# Add CORS middleware for frontend integration
allowed_origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in allowed_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "AI Personal Stylist API",
        "version": "1.0.0",
        "endpoints": [
            "/api/vision/analyze - POST: Analyze selfie",
            "/api/recommendations/outfit - POST: Get outfit recommendations",
            "/api/tryon/render - POST: Virtual try-on",
            "/api/chat/message - POST: Chatbot query",
            "/docs - Interactive API documentation"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI Personal Stylist"}

# VISION ANALYSIS ENDPOINTS
@app.post("/api/vision/analyze", response_model=AnalysisResult)
async def analyze_image(image: UploadFile = File(...)):
    """Analyze a selfie image for skin tone, body type, pose, and lighting."""
    contents = await image.read()
    nparr = np.frombuffer(contents, np.uint8)
    bgr_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if bgr_image is None:
        return {
            "skin_tone": "neutral",
            "body_type": "average",
            "lighting": "good",
            "pose": {"keypoints": {}}
        }
    
    # Use vision pipeline for complete analysis
    analysis = vision_pipeline.analyze_complete(bgr_image)
    
    return {
        "skin_tone": analysis["skin_tone"],
        "body_type": analysis["body_type"],
        "lighting": analysis["lighting"],
        "pose": {"keypoints": analysis["keypoints"]}
    }

@app.post("/api/vision/extract-features")
async def extract_features(image: UploadFile = File(...)):
    """Extract facial and body features from image."""
    contents = await image.read()
    nparr = np.frombuffer(contents, np.uint8)
    bgr_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if bgr_image is None:
        return {"error": "Invalid image"}
    
    analysis = vision_pipeline.analyze_complete(bgr_image)
    return {
        "face_detected": analysis["face_detected"],
        "face_bbox": analysis["face_bbox"],
        "skin_tone": analysis["skin_tone"],
        "body_type": analysis["body_type"],
        "keypoints": analysis["keypoints"],
        "lighting": analysis["lighting"]
    }

# RECOMMENDATION ENDPOINTS
@app.post("/api/recommendations/outfit", response_model=OutfitRecommendationResponse)
async def recommend_outfits(req: OutfitRecommendationRequest):
    """Get outfit recommendations based on user analysis."""
    outfits = recommendation_engine.get_recommendations(
        skin_tone=req.skin_tone.value if hasattr(req.skin_tone, 'value') else req.skin_tone,
        body_type=req.body_type.value if hasattr(req.body_type, 'value') else req.body_type,
        mood=req.mood.value if hasattr(req.mood, 'value') else req.mood,
        top_n=req.top_n
    )
    
    return {"outfits": outfits}

@app.get("/api/recommendations/colors")
async def get_color_palette(skin_tone: str = "neutral"):
    """Get color palette recommendations based on skin tone."""
    return {
        "skin_tone": skin_tone,
        "colors": recommendation_engine.SKIN_TONE_COLORS.get(
            skin_tone.lower(),
            recommendation_engine.SKIN_TONE_COLORS["neutral"]
        )
    }

# VIRTUAL TRY-ON ENDPOINTS
@app.post("/api/tryon/render")
async def virtual_tryon_render(
    user_image: UploadFile = File(...),
    garment_id: str = Form(...)
):
    """Generate virtual try-on rendering."""
    contents = await user_image.read()
    nparr = np.frombuffer(contents, np.uint8)
    bgr_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if bgr_image is None:
        return {"error": "Invalid image"}
    
    # Create try-on overlay
    result_image = virtual_tryon.create_overlay(bgr_image, garment_id)
    result_base64 = virtual_tryon.encode_image(result_image)
    
    return {
        "status": "success",
        "garment_id": garment_id,
        "image": result_base64,
        "message": "Try-on rendering complete"
    }

@app.post("/api/tryon/process")
async def process_tryon_request(user_image: UploadFile = File(...), garment_id: str = Form(...)):
    """Process and render a virtual try-on request."""
    return await virtual_tryon_render(user_image, garment_id)

# CHATBOT ENDPOINTS
@app.post("/api/chat/message")
async def chatbot_message(req: ChatRequest):
    """Handle user queries via chatbot."""
    reply = chatbot.get_response(req.message)
    
    return {
        "session_id": req.session_id,
        "user_message": req.message,
        "reply": reply
    }

@app.get("/api/chat/history")
async def get_chat_history(session_id: str):
    """Get chat history for a session (placeholder)."""
    return {
        "session_id": session_id,
        "messages": [],
        "note": "Chat history storage not yet implemented"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
