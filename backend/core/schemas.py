from pydantic import BaseModel
from typing import List, Optional, Dict
from .enums import SkinTone, BodyType, Mood, Occasion, LightingQuality

class PoseLandmarks(BaseModel):
    keypoints: Dict[str, Dict[str, float]]

class AnalysisResult(BaseModel):
    skin_tone: SkinTone
    body_type: BodyType
    lighting: LightingQuality
    pose: PoseLandmarks

class OutfitItem(BaseModel):
    top: str
    bottom: str
    style: str
    confidence: float
    color_palette: List[str]

class OutfitRecommendationRequest(BaseModel):
    skin_tone: SkinTone
    body_type: BodyType
    mood: Mood
    occasion: Occasion
    top_n: int = 3

class OutfitRecommendationResponse(BaseModel):
    outfits: List[OutfitItem]

class TryOnRequest(BaseModel):
    user_image_id: str
    garment_id: str

class ChatRequest(BaseModel):
    session_id: str
    message: str
