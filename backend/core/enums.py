from enum import Enum

class SkinTone(Enum):
    WARM = "warm"
    COOL = "cool"
    NEUTRAL = "neutral"

class BodyType(Enum):
    ATHLETIC = "athletic"
    SLIM = "slim"
    AVERAGE = "average"
    BROAD = "broad"

class Mood(Enum):
    CASUAL = "casual"
    OFFICE = "office"
    DATE_NIGHT = "date_night"
    WEDDING = "wedding"
    STREETWEAR = "streetwear"
    PARTY = "party"

class Occasion(Enum):
    CASUAL = "casual"
    OFFICE = "office"
    DATE = "date"
    FORMAL = "formal"
    WEDDING = "wedding"
    PARTY = "party"

class LightingQuality(Enum):
    GOOD = "good"
    LOW = "low"
    BACKLIT = "backlit"
    MIXED = "mixed"
