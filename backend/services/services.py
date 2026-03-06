\"\"\"Complete Recommendation, Try-On, and Chatbot Services.\"\"\"
import base64
import json
from pathlib import Path
from typing import Dict, List

import cv2
import numpy as np


# RECOMMENDATION ENGINE
class RecommendationEngine:
    \"\"\"AI-powered outfit recommendation system with multi-factor scoring.\"\"\"

    SKIN_TONE_COLORS = {
        \"warm\": [\"olive\", \"mustard\", \"camel\", \"burgundy\", \"gold\", \"chocolate\"],
        \"cool\": [\"navy\", \"emerald\", \"silver\", \"royal_blue\", \"magenta\", \"fuchsia\"],
        \"neutral\": [\"black\", \"white\", \"grey\", \"teal\", \"pink\", \"lavender\"],
    }

    SCORING_WEIGHTS = {
        \"color_match\": 0.35,
        \"body_style_fit\": 0.25,
        \"trend_score\": 0.20,
        \"mood_relevance\": 0.20,
    }

    OUTFITS = [
        {
            \"id\": \"metro_minimalist\",
            \"top\": \"Tailored Minimalist Shirt\",
            \"bottom\": \"Cropped Smart Trousers\",
            \"style\": \"Smart Casual\",
            \"palette\": [\"navy\", \"white\", \"grey\", \"silver\"],
            \"mood_tags\": [\"office\", \"date_night\", \"formal\"],
            \"body_fit\": {\"athletic\": 0.9, \"slim\": 0.86, \"average\": 0.88, \"broad\": 0.84},
            \"combo\": \"shirt+trousers\",
            \"seasonal\": {\"spring\": 0.83, \"summer\": 0.79, \"fall\": 0.88, \"winter\": 0.9},
        },
        {
            \"id\": \"cozy_street_core\",
            \"top\": \"Structured Hoodie\",
            \"bottom\": \"Tapered Cargo Pants\",
            \"style\": \"Streetwear\",
            \"palette\": [\"olive\", \"black\", \"camel\", \"grey\"],
            \"mood_tags\": [\"casual\", \"streetwear\", \"travel\"],
            \"body_fit\": {\"athletic\": 0.87, \"slim\": 0.9, \"average\": 0.86, \"broad\": 0.88},
            \"combo\": \"hoodie+cargo\",
            \"seasonal\": {\"spring\": 0.72, \"summer\": 0.62, \"fall\": 0.9, \"winter\": 0.93},
        },
        {
            \"id\": \"modern_tailored\",
            \"top\": \"Single-Breasted Blazer\",
            \"bottom\": \"High-Rise Pleated Pants\",
            \"style\": \"Formal\",
            \"palette\": [\"black\", \"navy\", \"white\", \"burgundy\"],
            \"mood_tags\": [\"wedding\", \"office\", \"formal\"],
            \"body_fit\": {\"athletic\": 0.93, \"slim\": 0.83, \"average\": 0.9, \"broad\": 0.86},
            \"combo\": \"blazer+trousers\",
            \"seasonal\": {\"spring\": 0.8, \"summer\": 0.69, \"fall\": 0.9, \"winter\": 0.95},
        },
        {
            \"id\": \"resort_soft\",
            \"top\": \"Breathable Linen Tee\",
            \"bottom\": \"Relaxed Drawstring Pants\",
            \"style\": \"Relaxed\",
            \"palette\": [\"white\", \"light_blue\", \"pastel\", \"teal\"],
            \"mood_tags\": [\"casual\", \"vacation\", \"date_night\"],
            \"body_fit\": {\"athletic\": 0.82, \"slim\": 0.84, \"average\": 0.85, \"broad\": 0.81},
            \"combo\": \"tee+linen\",
            \"seasonal\": {\"spring\": 0.88, \"summer\": 0.95, \"fall\": 0.66, \"winter\": 0.45},
        },
        {
            \"id\": \"night_glam\",
            \"top\": \"Satin Statement Top\",
            \"bottom\": \"Sculpted Midi Skirt\",
            \"style\": \"Party\",
            \"palette\": [\"black\", \"red\", \"purple\", \"magenta\"],
            \"mood_tags\": [\"party\", \"date_night\", \"wedding\"],
            \"body_fit\": {\"athletic\": 0.84, \"slim\": 0.93, \"average\": 0.89, \"broad\": 0.85},
            \"combo\": \"top+skirt\",
            \"seasonal\": {\"spring\": 0.82, \"summer\": 0.78, \"fall\": 0.91, \"winter\": 0.9},
        },
    ]

    _dataset_stats_cache = None

    @classmethod
    def _dataset_stats(cls) -> Dict:
        \"\"\"Load processed fashion dataset statistics when available.\"\"\"
        if cls._dataset_stats_cache is not None:
            return cls._dataset_stats_cache

        stats_path = Path(__file__).resolve().parent.parent / \"data_pipeline\" / \"processed\" / \"fashion_statistics.json\"
        if stats_path.exists():
            cls._dataset_stats_cache = json.loads(stats_path.read_text())
        else:
            cls._dataset_stats_cache = {
                \"color_popularity\": {},
                \"combination_popularity\": {},
                \"seasonal_style_trends\": {},
            }
        return cls._dataset_stats_cache

    @classmethod
    def _color_score(cls, skin_tone: str, palette: List[str], color_popularity: Dict[str, float]) -> float:
        affinities = cls.SKIN_TONE_COLORS.get(skin_tone, cls.SKIN_TONE_COLORS[\"neutral\"])
        affinity_score = sum(1 for color in palette if color in affinities) / max(1, len(palette))
        popularity_score = np.mean([float(color_popularity.get(c, 0.45)) for c in palette])
        return float(np.clip(0.65 * affinity_score + 0.35 * popularity_score, 0.0, 1.0))

    @classmethod
    def _body_score(cls, body_type: str, body_fit: Dict[str, float]) -> float:
        return float(np.clip(body_fit.get(body_type, 0.78), 0.0, 1.0))

    @classmethod
    def _trend_score(
        cls,
        outfit: Dict,
        mood: str,
        combination_popularity: Dict[str, float],
        seasonal_trends: Dict[str, Dict[str, float]],
        season: str,
    ) -> float:
        combo_score = float(combination_popularity.get(outfit[\"combo\"], 0.55))
        seasonal_style = seasonal_trends.get(season, {})
        seasonal_score = float(seasonal_style.get(outfit[\"style\"], outfit[\"seasonal\"].get(season, 0.7)))
        mood_boost = 0.1 if mood in outfit[\"mood_tags\"] else 0.0
        return float(np.clip(0.45 * combo_score + 0.45 * seasonal_score + mood_boost, 0.0, 1.0))

    @classmethod
    def _mood_score(cls, mood: str, mood_tags: List[str]) -> float:
        if mood in mood_tags:
            return 0.95
        if any(part in mood_tags for part in mood.split(\"_\")):
            return 0.82
        return 0.68

    @classmethod
    def get_recommendations(
        cls,
        skin_tone: str,
        body_type: str,
        mood: str,
        top_n: int = 3,
        season: str = \"spring\",
    ) -> List[Dict]:
        \"\"\"Get ranked outfit recommendations with an explainable scoring breakdown.\"\"\"
        stats = cls._dataset_stats()
        color_popularity = stats.get(\"color_popularity\", {})
        combination_popularity = stats.get(\"combination_popularity\", {})
        seasonal_trends = stats.get(\"seasonal_style_trends\", {})

        ranked = []
        for outfit in cls.OUTFITS:
            color_match = cls._color_score(skin_tone, outfit[\"palette\"], color_popularity)
            body_style_fit = cls._body_score(body_type, outfit[\"body_fit\"])
            trend_score = cls._trend_score(
                outfit, mood, combination_popularity, seasonal_trends, season
            )
            mood_relevance = cls._mood_score(mood, outfit[\"mood_tags\"])

            score = (
                cls.SCORING_WEIGHTS[\"color_match\"] * color_match
                + cls.SCORING_WEIGHTS[\"body_style_fit\"] * body_style_fit
                + cls.SCORING_WEIGHTS[\"trend_score\"] * trend_score
                + cls.SCORING_WEIGHTS[\"mood_relevance\"] * mood_relevance
            )

            ranked.append(
                {
                    \"top\": outfit[\"top\"],
                    \"bottom\": outfit[\"bottom\"],
                    \"style\": outfit[\"style\"],
                    \"confidence\": round(float(score), 3),
                    \"color_palette\": outfit[\"palette\"],
                    \"fit\": max(outfit[\"body_fit\"], key=outfit[\"body_fit\"].get),
                    \"score_breakdown\": {
                        \"color_match\": round(float(color_match), 3),
                        \"body_style_fit\": round(float(body_style_fit), 3),
                        \"trend_score\": round(float(trend_score), 3),
                        \"mood_relevance\": round(float(mood_relevance), 3),
                    },
                }
            )

        ranked.sort(key=lambda x: x[\"confidence\"], reverse=True)
        return ranked[:top_n]


# VIRTUAL TRY-ON ENGINE
class VirtualTryOn:
    \"\"\"Virtual clothing try-on system.\"\"\"

    GARMENT_DATABASE = {
        \"navy_shirt\": {\"type\": \"top\", \"color\": (80, 40, 10), \"opacity\": 0.8},
        \"white_shirt\": {\"type\": \"top\", \"color\": (255, 255, 255), \"opacity\": 0.95},
        \"black_hoodie\": {\"type\": \"top\", \"color\": (20, 20, 20), \"opacity\": 0.9},
        \"beige_chinos\": {\"type\": \"bottom\", \"color\": (220, 200, 170), \"opacity\": 0.85},
        \"blue_jeans\": {\"type\": \"bottom\", \"color\": (50, 80, 150), \"opacity\": 0.9},
        \"grey_pants\": {\"type\": \"bottom\", \"color\": (128, 128, 128), \"opacity\": 0.85},
    }

    @staticmethod
    def create_overlay(user_image: np.ndarray, garment_id: str) -> np.ndarray:
        \"\"\"Create virtual try-on overlay.\"\"\"
        h, w, _ = user_image.shape
        result = user_image.copy().astype(float)

        if garment_id not in VirtualTryOn.GARMENT_DATABASE:
            return user_image.astype(np.uint8)

        garment = VirtualTryOn.GARMENT_DATABASE[garment_id]
        color = np.array(garment[\"color\"], dtype=float)

        if garment[\"type\"] == \"top\":
            mask = np.zeros((h, w, 3), dtype=float)
            mask[: h // 2, :] = 1
        else:
            mask = np.zeros((h, w, 3), dtype=float)
            mask[h // 2 :, :] = 1

        opacity = garment[\"opacity\"]
        result = (1 - opacity) * result + opacity * mask * color

        return np.clip(result, 0, 255).astype(np.uint8)

    @staticmethod
    def encode_image(image: np.ndarray) -> str:
        \"\"\"Encode image to base64 for API response.\"\"\"
        _, buffer = cv2.imencode(\".jpg\", image)
        image_base64 = base64.b64encode(buffer).decode(\"utf-8\")
        return f\"data:image/jpeg;base64,{image_base64}\"


# CHATBOT ENGINE
class ChatbotEngine:
    \"\"\"AI stylist chatbot with fashion Q&A.\"\"\"

    RESPONSES = {
        \"party\": \"For a party, I recommend wearing bold colors and fitted clothing! Consider a dress or tailored outfit with statement accessories.\",
        \"office\": \"For office wear, smart casual is perfect! Go with an Oxford shirt or blouse paired with dress pants or a skirt.\",
        \"casual\": \"For casual outings, comfort is key! A simple tee with jeans or chinos works great.\",
        \"date\": \"For a date, smart casual shows effort! Try a nice shirt with chinos or a beautiful dress.\",
        \"wedding\": \"For a wedding, formal attire is essential! Consider a suit, blazer, or elegant dress in neutral or jewel tones.\",
        \"warm_tone\": \"Your warm skin tone pairs beautifully with earthy colors like mustard, olive, gold, and caramel!\",
        \"cool_tone\": \"Your cool skin tone looks amazing with jewel tones like navy, emerald, and silver!\",
        \"neutral_tone\": \"Your neutral skin tone is versatile! You can rock both warm and cool colors beautifully.\",
        \"athletic\": \"With your athletic body type, fitted clothing showcases your physique perfectly!\",
        \"slim\": \"With your slim body type, regular-fit and layered outfits create great proportions!\",
        \"broad\": \"With your broad shoulders, opt for relaxed fits and styles that balance your frame!\",
        \"how_it_works\": \"Our virtual try-on uses computer vision and MediaPipe pose detection to analyze your body, then overlays clothing items onto your image using perspective transforms and alpha blending!\",
        \"features\": \"Our AI Stylist features: skin tone analysis, body type estimation, mood-based recommendations, virtual try-on, and trend insights from big data!\",
    }

    @staticmethod
    def get_response(message: str) -> str:
        \"\"\"Generate chatbot response based on user message.\"\"\"
        message_lower = message.lower()

        for keyword, response in ChatbotEngine.RESPONSES.items():
            if keyword.replace(\"_\", \" \") in message_lower or keyword in message_lower:
                return response

        if \"recommend\" in message_lower:
            return \"I can help you find the perfect outfit! Tell me: what's the occasion (party, office, casual, wedding)?\"
        if \"color\" in message_lower:
            return \"Colors matter! Share your skin tone (warm, cool, neutral) and I'll suggest perfect colors for you.\"
        if \"body\" in message_lower:
            return \"Body type affects fit! Let me know your body shape (athletic, slim, average, broad) for better recommendations.\"
        if \"try\" in message_lower or \"try-on\" in message_lower:
            return \"Upload a selfie and choose a clothing item to see the virtual try-on preview!\"

        return \"I'm your AI Stylist! Ask me about outfit recommendations, color matching, or how our virtual try-on works!\"


# Global instances
recommendation_engine = RecommendationEngine()
virtual_tryon = VirtualTryOn()
chatbot = ChatbotEngine()
