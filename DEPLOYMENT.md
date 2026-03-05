# Deployment Guide

## Frontend Deployment (Vercel)

### Prerequisites
- Vercel account (vercel.com)
- GitHub account with repository access

### Steps
1. Push code to GitHub
2. Go to vercel.com and sign in
3. Click "New Project"
4. Import the `ai-personal-stylist-vton` repository
5. Configure project:
   - Framework: Vite
   - Root Directory: ./frontend
   - Build Command: npm run build
   - Output Directory: dist
6. Add environment variables if needed
7. Click Deploy

### Environment Variables (Vercel)
None required for basic functionality. For backend integration, add:
```
VITE_API_URL=https://your-backend-url.com
```

## Backend Deployment (Render)

### Prerequisites
- Render account (render.com)
- GitHub account with repository access

### Steps
1. Go to render.com and sign in
2. Click "New" → "Web Service"
3. Connect GitHub repository
4. Configure:
   - Name: ai-personal-stylist-api
   - Environment: Python 3.9
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn backend.app:app --host 0.0.0.0 --port 8000`
   - Root Directory: ./
5. Add environment variables:
   ```
   DATABASE_URL=your_db_url
   JWT_SECRET=your_secret_key
   CORS_ORIGINS=https://your-frontend-url.vercel.app
   ```
6. Deploy

### Environment Variables (Render)
```
CORS_ORIGINS=https://your-frontend-domain.vercel.app
```

## Testing Deployment

### Frontend
```
cd frontend
npm install
npm run build
npm run preview
```

### Backend
```
pip install -r requirements.txt
uvicorn backend.app:app --reload
```

Then navigate to http://localhost:8000/docs for API documentation.

## Troubleshooting

### CORS Issues
Update CORS origins in `backend/app.py` to match your frontend URL.

### Build Failures
- Check Node.js version compatibility
- Ensure all dependencies are installed
- Verify environment variables are set

## Live URLs
- Frontend: https://your-domain.vercel.app
- Backend API: https://your-api.onrender.com
- API Docs: https://your-api.onrender.com/docs
