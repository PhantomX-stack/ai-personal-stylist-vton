"""Complete Vision Pipeline for AI Personal Stylist."""
import cv2
import numpy as np
import mediapipe as mp
from typing import Dict, Optional, Tuple
import math

# MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

class VisionPipeline:
    """Complete computer vision pipeline for image analysis."""
    
    def __init__(self):
        self.face_detector = mp_face_detection.FaceDetection(
            model_selection=0, min_detection_confidence=0.5
        )
        self.pose_detector = mp_pose.Pose(
            static_image_mode=True, min_detection_confidence=0.5
        )
    
    def detect_face(self, bgr_image: np.ndarray) -> Optional[Tuple[int, int, int, int]]:
        """Detect face bounding box in image."""
        rgb = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        results = self.face_detector.process(rgb)
        
        if not results.detections:
            return None
        
        h, w, _ = bgr_image.shape
        detection = results.detections[0]
        bbox = detection.location_data.relative_bounding_box
        
        x = int(bbox.xmin * w)
        y = int(bbox.ymin * h)
        width = int(bbox.width * w)
        height = int(bbox.height * h)
        
        return (x, y, width, height)
    
    def segment_skin(self, bgr_image: np.ndarray) -> Optional[np.ndarray]:
        """Extract skin pixels from image using HSV."""
        hsv = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        
        # Skin tone ranges in HSV
        lower1 = np.array([0, 20, 70], dtype=np.uint8)
        upper1 = np.array([20, 255, 255], dtype=np.uint8)
        mask1 = cv2.inRange(hsv, lower1, upper1)
        
        lower2 = np.array([160, 20, 70], dtype=np.uint8)
        upper2 = np.array([179, 255, 255], dtype=np.uint8)
        mask2 = cv2.inRange(hsv, lower2, upper2)
        
        mask = cv2.bitwise_or(mask1, mask2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
        
        skin_pixels = bgr_image[mask > 0]
        return skin_pixels if skin_pixels.size > 0 else None
    
    def classify_skin_tone(self, bgr_image: np.ndarray) -> str:
        """Classify skin tone as warm, cool, or neutral."""
        skin_pixels = self.segment_skin(bgr_image)
        if skin_pixels is None:
            return "neutral"
        
        # Convert to RGB for analysis
        rgb_pixels = cv2.cvtColor(skin_pixels.reshape(-1, 1, 3), cv2.COLOR_BGR2RGB)
        mean_rgb = rgb_pixels.mean(axis=0).flatten() / 255.0
        r, g, b = mean_rgb
        
        # Classify based on color channels
        if r > (b + 0.05) and g > (b + 0.02):
            return "warm"
        elif b > (r + 0.05):
            return "cool"
        else:
            return "neutral"
    
    def estimate_pose(self, bgr_image: np.ndarray) -> Dict[str, Dict[str, float]]:
        """Extract pose landmarks using MediaPipe."""
        rgb = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        results = self.pose_detector.process(rgb)
        
        keypoints = {}
        if results.pose_landmarks:
            h, w, _ = bgr_image.shape
            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                if landmark.visibility > 0.5:
                    keypoints[str(idx)] = {
                        "x": landmark.x * w,
                        "y": landmark.y * h,
                        "z": landmark.z,
                        "visibility": landmark.visibility
                    }
        return keypoints
    
    def estimate_body_type(self, keypoints: Dict[str, Dict[str, float]]) -> str:
        """Estimate body type based on pose landmarks."""
        try:
            # Key indices: shoulders (11,12), hips (23,24), knees (25,26)
            if "11" not in keypoints or "12" not in keypoints or "23" not in keypoints or "24" not in keypoints:
                return "average"
            
            left_shoulder = (keypoints["11"]["x"], keypoints["11"]["y"])
            right_shoulder = (keypoints["12"]["x"], keypoints["12"]["y"])
            left_hip = (keypoints["23"]["x"], keypoints["23"]["y"])
            right_hip = (keypoints["24"]["x"], keypoints["24"]["y"])
            
            # Calculate widths
            shoulder_width = math.hypot(right_shoulder[0] - left_shoulder[0], right_shoulder[1] - left_shoulder[1])
            hip_width = math.hypot(right_hip[0] - left_hip[0], right_hip[1] - left_hip[1])
            
            if hip_width == 0:
                return "average"
            
            ratio = shoulder_width / hip_width
            
            if ratio > 1.15:
                return "athletic"
            elif ratio < 0.95:
                return "slim"
            elif ratio > 1.25:
                return "broad"
            else:
                return "average"
        except (KeyError, ValueError):
            return "average"
    
    def analyze_lighting(self, bgr_image: np.ndarray) -> str:
        """Analyze image lighting quality."""
        gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        mean_brightness = float(gray.mean())
        contrast = float(gray.std())
        
        if mean_brightness < 60:
            return "low"
        elif mean_brightness > 200:
            return "backlit"
        elif contrast < 25:
            return "mixed"
        else:
            return "good"
    
    def analyze_complete(self, bgr_image: np.ndarray) -> Dict:
        """Run complete analysis pipeline."""
        face_bbox = self.detect_face(bgr_image)
        skin_tone = self.classify_skin_tone(bgr_image)
        keypoints = self.estimate_pose(bgr_image)
        body_type = self.estimate_body_type(keypoints)
        lighting = self.analyze_lighting(bgr_image)
        
        return {
            "face_detected": face_bbox is not None,
            "face_bbox": face_bbox,
            "skin_tone": skin_tone,
            "keypoints": keypoints,
            "body_type": body_type,
            "lighting": lighting
        }

# Global instance
vision_pipeline = VisionPipeline()
