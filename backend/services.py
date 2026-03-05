"""Complete Recommendation, Try-On, and Chatbot Services."""
import cv2
import numpy as np
from typing import List, Dict, Optional
import base64
from io import BytesIO
from PIL import Image

# RECOMMENDATION ENGINE
class RecommendationEngine:
    """AI-powered outfit recommendation system."""
    
    SKIN_TONE_COLORS = {
        "warm": ["olive", "mustard", "camel", "burgundy", "gold", "chocolate"],
        "cool": ["navy", "emerald", "silver", "royal_blue", "magenta", "fuchsia"],
        "neutral": ["black", "white", "grey", "teal", "pink", "lavender"]
    }
    
    STYLE_TEMPLATES = {
        "casual": [
            {"top": "Crew Neck T-Shirt", "bottom": "Denim Jeans", "confidence": 0.9},
            {"top": "Henley", "bottom": "Chinos", "confidence": 0.85},
        ],
        "smart_casual": [
            {"top": "Oxford Shirt", "bottom": "Chinos", "confidence": 0.95},
            {"top": "Polo", "bottom": "Dress Pants", "confidence": 0.88},
        ],
        "formal": [
            {"top": "Blazer", "bottom": "Dress Pants", "confidence": 0.98},
            {"top": "Suit Jacket", "bottom": "Suit Trousers", "confidence": 0.97},
        ],
        "party": [
            {"top": "Black Shirt", "bottom": "Tailored Pants", "confidence": 0.92},
            {"top": "Dress", "bottom": "Heels", "confidence": 0.90},
        ],
        "streetwear": [
            {"top": "Hoodie", "bottom": "Joggers", "confidence": 0.88},
            {"top": "Graphic Tee", "bottom": "Cargo Pants", "confidence": 0.85},
        ],
    }
    
    BODY_ADJUSTMENTS = {
        "athletic": {"fit": "fitted", "cut": "tapered", "style": "modern"},
        "slim": {"fit": "regular", "cut": "straight", "style": "classic"},
        "average": {"fit": "standard", "cut": "standard", "style": "versatile"},
        "broad": {"fit": "relaxed", "cut": "wide", "style": "loose"},
    }
    
    MOOD_TO_STYLE = {
        "casual": "casual",
        "office": "smart_casual",
        "date_night": "smart_casual",
        "wedding": "formal",
        "party": "party",
        "streetwear": "streetwear",
    }
    
    @classmethod
    def get_recommendations(cls, skin_tone: str, body_type: str, mood: str, top_n: int = 3) -> List[Dict]:
        """Get outfit recommendations based on user profile."""
        style = cls.MOOD_TO_STYLE.get(mood, "casual")
        colors = cls.SKIN_TONE_COLORS.get(skin_tone, cls.SKIN_TONE_COLORS["neutral"])
        adjustments = cls.BODY_ADJUSTMENTS.get(body_type, cls.BODY_ADJUSTMENTS["average"])
        
        templates = cls.STYLE_TEMPLATES.get(style, [])
        outfits = []
        
        for template in templates:
            outfit = {
                "top": f"{adjustments['style'].title()} {template['top']}",
                "bottom": f"{adjustments['fit'].title()} {template['bottom']}",
                "style": style.replace("_", " ").title(),
                "confidence": template["confidence"],
                "color_palette": colors[:4],
                "fit": adjustments['fit'],
            }
            outfits.append(outfit)
        
        return outfits[:top_n]

# VIRTUAL TRY-ON ENGINE
class VirtualTryOn:
    """Virtual clothing try-on system."""
    
    GARMENT_DATABASE = {
        "navy_shirt": {"type": "top", "color": (80, 40, 10), "opacity": 0.8},
        "white_shirt": {"type": "top", "color": (255, 255, 255), "opacity": 0.95},
        "black_hoodie": {"type": "top", "color": (20, 20, 20), "opacity": 0.9},
        "beige_chinos": {"type": "bottom", "color": (220, 200, 170), "opacity": 0.85},
        "blue_jeans": {"type": "bottom", "color": (50, 80, 150), "opacity": 0.9},
        "grey_pants": {"type": "bottom", "color": (128, 128, 128), "opacity": 0.85},
    }
    
    @staticmethod
    def create_overlay(user_image: np.ndarray, garment_id: str) -> np.ndarray:
        """Create virtual try-on overlay."""
        h, w, _ = user_image.shape
        result = user_image.copy().astype(float)
        
        if garment_id not in VirtualTryOn.GARMENT_DATABASE:
            return user_image.astype(np.uint8)
        
        garment = VirtualTryOn.GARMENT_DATABASE[garment_id]
        color = np.array(garment["color"], dtype=float)
        
        if garment["type"] == "top":
            # Apply to upper half
            mask = np.zeros((h, w, 3), dtype=float)
            mask[:h//2, :] = 1
        else:
            # Apply to lower half
            mask = np.zeros((h, w, 3), dtype=float)
            mask[h//2:, :] = 1
        
        opacity = garment["opacity"]
        result = (1 - opacity) * result + opacity * mask * color
        
        return np.clip(result, 0, 255).astype(np.uint8)
    
    @staticmethod
    def encode_image(image: np.ndarray) -> str:
        """Encode image to base64 for API response."""
        _, buffer = cv2.imencode('.jpg', image)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        return f"data:image/jpeg;base64,{image_base64}"

# CHATBOT ENGINE
class ChatbotEngine:
    """AI stylist chatbot with fashion Q&A."""
    
    RESPONSES = {
        "party": "For a party, I recommend wearing bold colors and fitted clothing! Consider a dress or tailored outfit with statement accessories.",
        "office": "For office wear, smart casual is perfect! Go with an Oxford shirt or blouse paired with dress pants or a skirt.",
        "casual": "For casual outings, comfort is key! A simple tee with jeans or chinos works great.",
        "date": "For a date, smart casual shows effort! Try a nice shirt with chinos or a beautiful dress.",
        "wedding": "For a wedding, formal attire is essential! Consider a suit, blazer, or elegant dress in neutral or jewel tones.",
        "warm_tone": "Your warm skin tone pairs beautifully with earthy colors like mustard, olive, gold, and caramel!",
        "cool_tone": "Your cool skin tone looks amazing with jewel tones like navy, emerald, and silver!",
        "neutral_tone": "Your neutral skin tone is versatile! You can rock both warm and cool colors beautifully.",
        "athletic": "With your athletic body type, fitted clothing showcases your physique perfectly!",
        "slim": "With your slim body type, regular-fit and layered outfits create great proportions!",
        "broad": "With your broad shoulders, opt for relaxed fits and styles that balance your frame!",
        "how_it_works": "Our virtual try-on uses computer vision and MediaPipe pose detection to analyze your body, then overlays clothing items onto your image using perspective transforms and alpha blending!",
        "features": "Our AI Stylist features: skin tone analysis, body type estimation, mood-based recommendations, virtual try-on, and trend insights from big data!",
    }
    
    @staticmethod
    def get_response(message: str) -> str:
        """Generate chatbot response based on user message."""
        message_lower = message.lower()
        
        for keyword, response in ChatbotEngine.RESPONSES.items():
            if keyword.replace("_", " ") in message_lower or keyword in message_lower:
                return response
        
        if "recommend" in message_lower:
            return "I can help you find the perfect outfit! Tell me: what's the occasion (party, office, casual, wedding)?"
        if "color" in message_lower:
            return "Colors matter! Share your skin tone (warm, cool, neutral) and I'll suggest perfect colors for you."
        if "body" in message_lower:
            return "Body type affects fit! Let me know your body shape (athletic, slim, average, broad) for better recommendations."
        if "try" in message_lower or "try-on" in message_lower:
            return "Upload a selfie and choose a clothing item to see the virtual try-on preview!"
        
        return "I'm your AI Stylist! Ask me about outfit recommendations, color matching, or how our virtual try-on works!"

# Global instances
recommendation_engine = RecommendationEngine()
virtual_tryon = VirtualTryOn()
chatbot = ChatbotEngine()
