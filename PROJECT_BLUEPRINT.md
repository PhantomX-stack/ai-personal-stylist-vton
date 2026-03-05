# Project Blueprint: Implementation Guide

## Overview
This document provides a step-by-step implementation guide for developers building out the AI Personal Stylist & Virtual Try-On system.

## Phase 1: Core Infrastructure (Weeks 1-2)

### 1.1 Vision Pipeline Implementation

**File: `services/vision/face_detection.py`**
```python
# Use OpenCV cascade classifiers or MediaPipe Face Detection
# Task: Locate face bounding box in image
# Output: (x, y, w, h) tuple
# Fallback: Return None if no face detected
```

**File: `services/vision/skin_segmentation.py`**
```python
# Use HSV color space thresholding
# 1. Convert BGR to HSV
# 2. Define skin tone ranges (tune per skin diversity)
# 3. Apply morphological operations (erode/dilate)
# 4. Extract skin pixels from face region
# 5. Return masked array of skin colors
```

**File: `services/vision/skin_tone_classifier.py`**
```python
# Classify RGB features into warm/cool/neutral
# Baseline: Compare R, G, B channel means
#   - Warm: high red/yellow (R+G > B + threshold)
#   - Cool: high blue (B > R + threshold)
#   - Neutral: balanced
# Future: Train CNN on Fitzpatrick scale data
```

**File: `services/vision/pose_estimation.py`**
```python
# Use MediaPipe Pose (33 landmarks) or OpenPose (18 landmarks)
# Extract: nose, shoulders, hips, knees, ankles
# Return: PoseLandmarks schema with x, y, z coordinates
# Confidence filtering: discard landmarks with low visibility
```

**File: `services/vision/body_type_estimator.py`**
```python
# Calculate ratios from pose landmarks:
#   - shoulder_width / hip_width
#   - torso_height / leg_height
# Thresholds (tune on labeled data):
#   - Athletic: shoulder_width > 1.15 * hip_width, lean torso
#   - Slim: wide hip-to-shoulder, longer legs
#   - Broad: very wide shoulders
#   - Average: balanced proportions
```

**File: `services/vision/lighting_analysis.py`**
```python
# Compute histogram and basic statistics
# Metrics:
#   - Mean brightness (dark < 60, bright > 200)
#   - Standard deviation (uniform < 25 = flat/bad)
#   - Contrast ratio (Michelson contrast)
# Return: LightingQuality enum
```

### 1.2 API Integration
Update `backend/app.py` endpoints to call vision functions:
```python
@app.post("/analyze")
async def analyze_image(image: UploadFile):
    bgr = read_image(image)
    skin_tone = classify_skin_tone(bgr)
    pose = estimate_pose(bgr)
    body_type = estimate_body_type(pose)
    lighting = analyze_lighting(bgr)
    return AnalysisResult(...)
```

---

## Phase 2: Recommendation Engine (Weeks 3-4)

### 2.1 Color Mapping

**File: `services/recommendation/color_rules_engine.py`**
```python
# Hardcoded color palettes (research-backed from style guides)
SKIN_TONE_COLOR_PALETTES = {
    SkinTone.WARM: [...colors...],
    SkinTone.COOL: [...colors...],
    SkinTone.NEUTRAL: [...colors...]
}
```

### 2.2 Mood & Style Mapping

**File: `services/recommendation/mood_style_mapping.py`**
```python
# Map mood/occasion to base fashion styles
def get_base_styles(mood, occasion) -> List[str]:
    # Examples: "casual", "smart casual", "formal", "party", etc.
    pass

STYLE_TEMPLATES = {
    "smart casual": [
        {"top": "navy shirt", "bottom": "beige chinos"},
        {...},
    ],
    "streetwear": [...],
    # ...
}
```

### 2.3 Body-Type Adjustments

**File: `services/recommendation/body_style_rules.py`**
```python
# Modify garment descriptions based on body type
# Athletic: replace "oversized" -> "fitted"
# Slim: replace "fitted" -> "regular fit"
# Broad: use v-necks, avoid crew necks
# etc.
```

### 2.4 Outfit Ranker

**File: `services/recommendation/outfit_ranker.py`**
```python
# Scoring function:
# score = alpha * tone_match + beta * global_popularity + gamma * cooccurrence
#
# tone_match: does outfit contain recommended colors?
# global_popularity: from Hadoop stats (color_trends.parquet)
# cooccurrence: are top+bottom pairs common? (from outfit_stats.parquet)
#
# Rank candidates and return top_n
```

### 2.5 Hadoop Integration

**File: `data_pipeline/hadoop/mapreduce_color_trends.py`**
```python
# Mapper: extract color from each item, emit count
# Reducer: sum counts per color
# Output: parquet with color -> total_purchases/views

# Load into recommendation engine at startup:
# GLOBAL_COLOR_TRENDS = pd.read_parquet(...).to_dict()
```

---

## Phase 3: Virtual Try-On (Weeks 5-6)

### 3.1 Garment Asset Management

**File: `services/tryon/garment_assets.py`**
```python
GARMENT_DB = {
    "navy_shirt": "assets/garments/navy_shirt.png",  # RGBA
    "beige_chinos": "assets/garments/beige_chinos.png",
    # ...
}

def load_garment_image(garment_id) -> np.ndarray:
    # Load RGBA image (transparent background)
    return cv2.imread(GARMENT_DB[garment_id], cv2.IMREAD_UNCHANGED)
```

### 3.2 Pose to Mesh

**File: `services/tryon/pose_to_mesh.py`**
```python
# Extract torso polygon from pose landmarks
def compute_torso_polygon(pose: PoseLandmarks) -> np.ndarray:
    # Connect: left_shoulder, right_shoulder, right_hip, left_hip
    # Return 4-point polygon in image coordinates
    pass

# Future: full body mesh with shoulders, arms, torso, legs
```

### 3.3 Warping

**File: `services/tryon/warping.py`**
```python
# Geometric alignment of garment to body
def warp_garment_to_torso(
    garment_rgba: np.ndarray,
    src_poly: np.ndarray,  # garment corners
    dst_poly: np.ndarray,  # user torso polygon
    output_shape: tuple
) -> np.ndarray:
    # Use cv2.getPerspectiveTransform (4-point) or TPS (more flexible)
    M = cv2.getPerspectiveTransform(src_poly, dst_poly)
    warped = cv2.warpPerspective(garment_rgba, M, output_shape)
    return warped
```

### 3.4 Rendering

**File: `services/tryon/renderer.py`**
```python
def alpha_blend(base_bgr, overlay_rgba) -> np.ndarray:
    # Extract alpha channel, use for blending
    # result = alpha * overlay + (1 - alpha) * base
    pass

def render_tryon(user_bgr, garment_rgba) -> np.ndarray:
    # Warp + alpha blend
    return alpha_blend(user_bgr, garment_rgba)
```

---

## Phase 4: Chatbot (Week 7)

**File: `services/chatbot/dialogue_manager.py`**
```python
def handle_chat(req: ChatRequest) -> str:
    # Simple intent parsing (keyword-based)
    #   "party" -> Mood.PARTY
    #   "office" -> Mood.OFFICE
    #   etc.
    #
    # Later: use LLM (GPT-3.5, Claude) for semantic understanding
    # Trigger recommendation + try-on workflows
    pass
```

---

## Testing Strategy

### Unit Tests
```bash
pytest services/vision/test_skin_tone.py
pytest services/recommendation/test_outfit_ranker.py
pytest services/tryon/test_warping.py
```

### Integration Tests
```bash
# Test full pipeline
pytest tests/test_e2e.py
```

### Performance Benchmarks
```bash
python benchmarks/benchmark_vision_pipeline.py
python benchmarks/benchmark_recommendation.py
```

---

## Deployment

### Local Development
```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Docker
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0"]
```

### Kubernetes
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-stylist
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: api
        image: ai-personal-stylist:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "2Gi"
            cpu: "1"
```

---

## Next Steps
1. Implement Phase 1 (Vision) with unit tests
2. Integrate with FastAPI endpoints
3. Test with real selfie images
4. Proceed to Phase 2 (Recommendations)
5. Integrate Hadoop big-data stats
6. Implement Phase 3 (Try-On)
7. Polish UI/UX

---

## Resources
- MediaPipe Pose: https://mediapipe.dev/
- OpenCV Docs: https://docs.opencv.org/
- Hadoop MapReduce: https://hadoop.apache.org/
- FastAPI: https://fastapi.tiangolo.com/
- Virtual Try-On Papers: VITON, ClothFlow, etc.
