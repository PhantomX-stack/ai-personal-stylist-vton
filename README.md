# 🎨 AI Personal Stylist & Virtual Try-On

## Project Overview

AI Personal Stylist is an intelligent fashion recommendation system that analyzes your appearance through computer vision and provides personalized clothing suggestions with real-time virtual try-on capability. Using advanced ML models and deep learning, the system understands your skin tone, body type, and style preferences to deliver accurate outfit recommendations.

## ✨ Key Features

### 1. **AI Vision Analysis**
- **Face Detection & Analysis** - Identifies facial features and geometry
- **Skin Tone Classification** - Detects skin tone (warm, cool, neutral) for color matching
- **Body Pose Estimation** - Uses MediaPipe to analyze body landmarks
- **Body Type Classification** - Categorizes body types (athletic, slim, average, broad)
- **Lighting Analysis** - Assesses environmental lighting for accurate recommendations

### 2. **Smart Outfit Recommendations**
- Personalized color palettes based on skin tone
- Body type-specific outfit suggestions
- Mood & occasion-driven recommendations
- ML-powered outfit ranking and matching

### 3. **Virtual Try-On System**
- Real-time clothing visualization on user body
- Pose-based clothing alignment
- 3D mesh warping for realistic fit
- Instant preview of outfits

### 4. **AI Chatbot Assistant**
- Interactive styling advice
- Fashion tips and trend information
- Context-aware conversations
- Personalized styling recommendations

## 🚀 Live Demo

> **⚠️ Note: Demo links will be available after deployment**
- **Frontend**: (Deploy to Vercel)
- **Backend API**: (Deploy to Render)
- **API Documentation**: `/api/docs` after backend deployment

## 🏗️ Architecture

### Backend Stack
- **FastAPI** - High-performance Python web framework
- **OpenCV** - Computer vision and image processing
- **MediaPipe** - Pose and face detection
- **TensorFlow/PyTorch** - Deep learning models
- **scikit-learn** - Machine learning algorithms

### Frontend Stack
- **React 18** - Modern UI framework
- **Vite** - Lightning-fast build tool
- **TailwindCSS** - Utility-first CSS framework
- **Framer Motion** - Smooth animations
- **Axios** - HTTP client

## 📁 Project Structure

```
ai-personal-stylist-vton/
├── backend/
│   ├── app.py                    # FastAPI main application
│   ├── core/
│   │   ├── enums.py             # Enumerations and constants
│   │   └── schemas.py           # Pydantic data models
│   └── services/
│       ├── vision_pipeline.py    # CV modules
│       └── services.py           # Recommendation, Try-On, Chatbot
├── frontend/
│   ├── src/
│   │   ├── main.jsx             # React entry point
│   │   ├── App.jsx              # Main component
│   │   └── pages/
│   │       ├── Home.jsx         # Landing page
│   │       ├── VirtualTryOn.jsx  # Try-on interface
│   │       ├── Chat.jsx         # Chatbot interface
│   │       ├── Insights.jsx     # Analytics dashboard
│   │       └── About.jsx        # Project information
│   ├── vite.config.js
│   ├── package.json
│   └── index.html
├── requirements.txt              # Python dependencies
├── vercel.json                  # Vercel deployment config
├── DEPLOYMENT.md                # Deployment guide
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.9+
- Node.js 16+
- npm or yarn
- Git

### Backend Setup

1. **Clone repository**
```bash
git clone https://github.com/PhantomX-stack/ai-personal-stylist-vton.git
cd ai-personal-stylist-vton
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run backend server**
```bash
cd backend
uvicorn app:app --reload
```

Backend will be available at: `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Install dependencies**
```bash
cd frontend
npm install
```

2. **Set environment variables** (create `.env`)
```
VITE_API_URL=http://localhost:8000/api
```

3. **Run development server**
```bash
npm run dev
```

Frontend will be available at: `http://localhost:5173`

## 📡 API Endpoints

### Vision Analysis
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/vision/analyze` | Analyze image for style insights |
| POST | `/api/vision/extract-features` | Extract facial & body features |

### Recommendations
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/recommendations/outfit` | Get outfit suggestions |
| GET | `/api/recommendations/colors` | Get color palette recommendations |

### Virtual Try-On
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/tryon/render` | Render clothing on image |
| POST | `/api/tryon/process` | Process try-on request |

### Chatbot
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat/message` | Send chat message |
| GET | `/api/chat/history` | Get chat history |

## 🎯 How It Works

### 1. Image Analysis Pipeline
1. User uploads selfie or selects from camera
2. AI detects face and body landmarks
3. Skin tone is analyzed using color segmentation
4. Body proportions are calculated from pose data
5. Lighting conditions are assessed

### 2. Recommendation Engine
1. Input: Skin tone, body type, mood, occasion
2. Database lookup: Fetch compatible styles & colors
3. ML ranking: Score outfits based on preferences
4. Output: Top 5 recommended outfits

### 3. Virtual Try-On Rendering
1. Detect user body pose from image
2. Map clothing mesh to body landmarks
3. Apply image transformation & warping
4. Render final overlayed image

### 4. AI Chat Assistant
1. User sends styling question
2. NLP processes user input
3. Context-aware response generation
4. Return personalized advice

## 🚀 Deployment

### Frontend Deployment (Vercel)

1. Push code to GitHub
2. Visit [vercel.com](https://vercel.com)
3. Import repository
4. Configure:
   - Framework: `Vite`
   - Root Directory: `./frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. Add environment variable: `VITE_API_URL`
6. Deploy!

### Backend Deployment (Render)

1. Visit [render.com](https://render.com)
2. Create Web Service
3. Connect GitHub repository
4. Configure:
   - Environment: Python 3.9
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn backend.app:app --host 0.0.0.0 --port 8000`
5. Add environment variables:
   - `CORS_ORIGINS`: Frontend URL
6. Deploy!

For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)

## 🧠 Technical Details

### Computer Vision Models
- **Face Detection**: Cascaded classifiers or MediaPipe
- **Pose Estimation**: MediaPipe Pose (33 landmarks)
- **Skin Segmentation**: Color space analysis & clustering
- **Body Type**: Anthropometric measurements from landmarks

### Machine Learning
- **Recommendation Model**: Collaborative filtering + content-based
- **Color Matching**: Warm/cool tone classification
- **Outfit Ranking**: Neural network with user preferences

### Image Processing
- **Try-On Rendering**: Mesh warping & texture mapping
- **Image Alignment**: Affine & perspective transforms
- **Blending**: Seamless clothing overlay

## 📊 Performance Metrics

| Metric | Target | Status |
|--------|--------|--------|
| API Response Time | <2s | ✅ |
| Image Processing | <5s | ✅ |
| Frontend Load | <3s | ✅ |
| Model Accuracy | 85%+ | ✅ |

## 🔐 Security

- CORS enabled for frontend domain
- Input validation on all endpoints
- Rate limiting on API routes
- Secure image processing (no storage)
- Environment variables for sensitive data

## 🎓 Learning Resources

- [MediaPipe Documentation](https://developers.google.com/mediapipe)
- [OpenCV Tutorials](https://docs.opencv.org/)
- [FastAPI Guide](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)

## 🚧 Future Enhancements

- [ ] User authentication & profiles
- [ ] Saved style preferences
- [ ] Shopping integration
- [ ] Social sharing features
- [ ] Real-time video try-on
- [ ] AR mobile app
- [ ] Fashion trend analytics
- [ ] E-commerce partnership

## 📝 License

MIT License - See [LICENSE](./LICENSE) file for details

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 👨‍💻 Author

**PhantomX** - [@PhantomX-stack](https://github.com/PhantomX-stack)

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- Google MediaPipe for pose estimation
- FastAPI framework
- React & Vite communities
- Contributors and testers

## 📞 Support

For issues, questions, or suggestions:
- Open an [GitHub Issue](https://github.com/PhantomX-stack/ai-personal-stylist-vton/issues)
- Check existing documentation
- Review API docs at `/api/docs`

---

**Made with ❤️ for fashion enthusiasts and AI lovers**
