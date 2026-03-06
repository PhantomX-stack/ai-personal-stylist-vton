"""Advanced AI Recommendation Engine V2

Implements intelligent outfit recommendation using weighted scoring system.
Factors: color compatibility, body type fit, trend analysis, mood relevance.
"""

import numpy as np
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class OutfitScore:
    """Outfit with detailed scoring breakdown"""
    name: str
    confidence: float
    color_score: float
    body_score: float
    trend_score: float
    mood_score: float
    
    @property
    def weighted_score(self) -> float:
        """Calculate final weighted score"""
        return (0.35 * self.color_score +
                0.25 * self.body_score +
                0.20 * self.trend_score +
                0.20 * self.mood_score)

class AdvancedRecommendationEngine:
    """Next-generation outfit recommendation system"""
    
    # Comprehensive outfit database with attributes
    OUTFIT_DATABASE = {
        "classic_blue_shirt": {
            "colors": ["navy", "white"],
            "body_fit": {"athletic": 0.9, "slim": 0.7, "average": 0.85, "broad": 0.8},
            "trend_score": 0.85,
            "occasions": ["office", "casual", "date"],
            "seasons": ["spring", "summer", "fall", "winter"]
        },
        "casual_hoodie": {
            "colors": ["black", "grey", "olive"],
            "body_fit": {"athletic": 0.8, "slim": 0.9, "average": 0.85, "broad": 0.9},
            "trend_score": 0.90,
            "occasions": ["casual", "streetwear"],
            "seasons": ["fall", "winter"]
        },
        "formal_blazer": {
            "colors": ["black", "navy", "grey"],
            "body_fit": {"athletic": 0.95, "slim": 0.75, "average": 0.88, "broad": 0.85},
            "trend_score": 0.88,
            "occasions": ["office", "wedding", "formal"],
            "seasons": ["fall", "winter", "spring"]
        },
        "summer_tee": {
            "colors": ["white", "light_blue", "pastel"],
            "body_fit": {"athletic": 0.85, "slim": 0.8, "average": 0.8, "broad": 0.75},
            "trend_score": 0.82,
            "occasions": ["casual"],
            "seasons": ["spring", "summer"]
        },
        "party_dress": {
            "colors": ["black", "red", "purple"],
            "body_fit": {"athletic": 0.8, "slim": 0.95, "average": 0.9, "broad": 0.85},
            "trend_score": 0.92,
            "occasions": ["party", "wedding", "date"],
            "seasons": ["fall", "winter", "spring"]
        }
    }
    
    # Color compatibility matrix
    SKIN_TONE_COLOR_AFFINITY = {
        "warm": {
            "navy": 0.7, "olive": 0.95, "mustard": 0.95,
            "camel": 0.9, "burgundy": 0.85, "gold": 0.9,
            "chocolate": 0.88, "orange": 0.92, "terracotta": 0.93,
            "black": 0.75, "white": 0.8, "grey": 0.75
        },
        "cool": {
            "navy": 0.95, "emerald": 0.92, "silver": 0.9,
            "royal_blue": 0.93, "magenta": 0.88, "fuchsia": 0.9,
            "purple": 0.92, "red": 0.85, "pink": 0.88,
            "black": 0.9, "white": 0.92, "grey": 0.85
        },
        "neutral": {
            "black": 0.95, "white": 0.95, "grey": 0.93,
            "navy": 0.9, "emerald": 0.85, "burgundy": 0.88,
            "teal": 0.9, "pink": 0.85, "lavender": 0.87,
            "olive": 0.88, "camel": 0.85, "gold": 0.85
        }
    }
    
    # Trend scores by season
    TREND_BOOST = {
        "spring": {"pastels": 0.15, "floral": 0.12, "light_fabrics": 0.1},
        "summer": {"white": 0.15, "shorts": 0.12, "sundresses": 0.15},
        "fall": {"earth_tones": 0.15, "layers": 0.12, "boots": 0.13},
        "winter": {"dark_colors": 0.15, "coats": 0.15, "wool": 0.12}
    }
    
    @classmethod
    def calculate_color_score(cls, skin_tone: str, outfit_colors: List[str]) -> float:
        """Calculate color compatibility score (0-1)"""
        if skin_tone not in cls.SKIN_TONE_COLOR_AFFINITY:
            return 0.5
        
        affinities = cls.SKIN_TONE_COLOR_AFFINITY[skin_tone]
        scores = [affinities.get(color, 0.5) for color in outfit_colors]
        return float(np.mean(scores)) if scores else 0.5
    
    @classmethod
    def calculate_body_score(cls, body_type: str, outfit_name: str) -> float:
        """Calculate body type suitability score (0-1)"""
        if outfit_name not in cls.OUTFIT_DATABASE:
            return 0.7
        
        outfit = cls.OUTFIT_DATABASE[outfit_name]
        return outfit["body_fit"].get(body_type, 0.7)
    
    @classmethod
    def calculate_trend_score(cls, outfit_name: str, season: str = "spring") -> float:
        """Calculate trend relevance score (0-1)"""
        if outfit_name not in cls.OUTFIT_DATABASE:
            return 0.7
        
        base_score = cls.OUTFIT_DATABASE[outfit_name]["trend_score"]
        season_boost = 0.1 if season in cls.OUTFIT_DATABASE[outfit_name]["seasons"] else 0
        return min(1.0, base_score + season_boost)
    
    @classmethod
    def calculate_mood_score(cls, outfit_name: str, mood: str) -> float:
        """Calculate mood/occasion relevance score (0-1)"""
        if outfit_name not in cls.OUTFIT_DATABASE:
            return 0.7
        
        outfit = cls.OUTFIT_DATABASE[outfit_name]
        base_score = 0.7
        
        if mood in outfit["occasions"]:
            base_score = 0.95
        elif any(mood_part in outfit["occasions"] for mood_part in mood.split("_")):
            base_score = 0.85
        
        return base_score
    
    @classmethod
    def get_recommendations(cls, 
                          skin_tone: str,
                          body_type: str,
                          mood: str,
                          season: str = "spring",
                          top_n: int = 3) -> List[OutfitScore]:
        """Get top N outfit recommendations with detailed scoring
        
        Args:
            skin_tone: warm, cool, or neutral
            body_type: athletic, slim, average, or broad
            mood: casual, office, date, wedding, party, etc.
            season: spring, summer, fall, or winter
            top_n: number of recommendations to return
            
        Returns:
            List of OutfitScore objects ranked by weighted score
        """
        
        recommendations = []
        
        for outfit_name in cls.OUTFIT_DATABASE:
            outfit_data = cls.OUTFIT_DATABASE[outfit_name]
            
            # Calculate individual scores
            color_score = cls.calculate_color_score(skin_tone, outfit_data["colors"])
            body_score = cls.calculate_body_score(body_type, outfit_name)
            trend_score = cls.calculate_trend_score(outfit_name, season)
            mood_score = cls.calculate_mood_score(outfit_name, mood)
            
            # Create recommendation
            rec = OutfitScore(
                name=outfit_name.replace("_", " ").title(),
                confidence=max(0.0, min(1.0, np.mean([color_score, body_score, trend_score, mood_score]))),
                color_score=color_score,
                body_score=body_score,
                trend_score=trend_score,
                mood_score=mood_score
            )
            
            recommendations.append(rec)
        
        # Sort by weighted score
        recommendations.sort(key=lambda x: x.weighted_score, reverse=True)
        
        return recommendations[:top_n]

# Global instance
advanced_engine = AdvancedRecommendationEngine()
