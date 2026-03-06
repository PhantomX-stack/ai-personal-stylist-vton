# Troubleshooting Guide

This guide helps you resolve common issues when using AI Personal Stylist & Virtual Try-On.

## Backend Issues

### Port Already in Use (Backend)

**Error:** `Address already in use` or `OSError: [Errno 48] Address already in use`

**Solutions:**

1. Check what's using port 8000:
   ```bash
   # On macOS/Linux:
   lsof -i :8000
   # On Windows:
   netstat -ano | findstr :8000
   ```

2. Kill the process:
   ```bash
   # On macOS/Linux:
   kill -9 <PID>
   # On Windows:
   taskkill /PID <PID> /F
   ```

3. Use a different port:
   ```bash
   uvicorn app:app --reload --port 8001
   ```

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'backend'`

**Solution:**
```bash
cd backend
pip install -r ../requirements.txt
# Make sure __init__.py files exist in all packages:
# backend/__init__.py
# backend/core/__init__.py
# backend/services/__init__.py
# backend/vision/__init__.py
```

### CORS Errors

**Error:** `Access to XMLHttpRequest has been blocked by CORS policy`

**Solution:**
1. Verify backend is running
2. Check CORS configuration in `backend/app.py`
3. Ensure `VITE_API_URL` is correctly set in frontend `.env`
4. Clear browser cache and try again

### Vision Analysis Timeout

**Error:** `Request timeout` when analyzing images

**Solutions:**
1. Ensure image size is reasonable (< 5MB)
2. Check if MediaPipe is properly installed:
   ```bash
   pip install mediapipe --upgrade
   ```
3. Verify GPU availability (if using GPU acceleration)
4. Increase timeout in frontend API calls

## Frontend Issues

### Port Already in Use (Frontend)

**Error:** `Port 5173 is already in use` or `Error: listen EADDRINUSE`

**Solutions:**

1. Use a different port:
   ```bash
   npm run dev -- --port 3000
   ```

2. Kill the process using the port:
   ```bash
   # On macOS/Linux:
   lsof -i :5173 | grep LISTEN | awk '{print $2}' | xargs kill -9
   # On Windows:
   netstat -ano | findstr :5173
   ```

### Module Not Found Errors

**Error:** `Cannot find module 'axios'` or similar

**Solution:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Environment Variables Not Loading

**Error:** API calls returning 404 or undefined

**Solution:**
1. Verify `.env` file exists in `frontend/` directory
2. Check that `VITE_API_URL` is set correctly
3. Rebuild frontend:
   ```bash
   npm run dev
   ```
4. Restart the dev server and clear cache

### Build Errors

**Error:** `npm run build` fails

**Solution:**
```bash
cd frontend
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Styling Not Applying

**Error:** Tailwind CSS styles not visible

**Solution:**
1. Verify tailwind configuration is correct
2. Clear browser cache (Ctrl+Shift+Delete)
3. Restart dev server
4. Check if tailwind config includes all template files

## Installation Issues

### Python Version Issues

**Error:** `Python 3.9 or higher required`

**Solution:**
```bash
python --version  # Check current version
# If version < 3.9, install Python 3.9+
# Then create a new virtual environment
python3.9 -m venv venv
```

### Node Version Issues

**Error:** `Node version should be 16+`

**Solution:**
```bash
node --version  # Check current version
# If version < 16, install Node 16+
# Visit https://nodejs.org/ for downloads
```

### Dependencies Conflict

**Error:** Dependency conflict warnings

**Solution:**
```bash
# For frontend:
cd frontend
npm install --legacy-peer-deps

# For backend:
cd backend
pip install --upgrade pip setuptools wheel
pip install -r ../requirements.txt
```

## Deployment Issues

### Vercel Deployment Fails

**Error:** Build fails on Vercel

**Solutions:**
1. Check build logs in Vercel dashboard
2. Ensure `.env` variables are set in Vercel settings
3. Verify build command: `npm run build`
4. Verify output directory: `dist`

### Render Deployment Fails

**Error:** Backend deployment fails on Render

**Solutions:**
1. Check Render logs
2. Verify Python version is 3.9+
3. Check environment variables are set
4. Ensure start command is correct:
   ```
   uvicorn backend.app:app --host 0.0.0.0 --port 8000
   ```

### Database Connection Issues

**Error:** Cannot connect to database

**Solution:** (When database is added)
1. Verify database URL in environment variables
2. Check database is running and accessible
3. Verify credentials are correct
4. Check firewall rules allow connection

## Performance Issues

### Slow API Response

**Problem:** API endpoints taking > 500ms

**Solutions:**
1. Check server logs for bottlenecks
2. Verify image size isn't too large
3. Check if ML models are loaded
4. Monitor CPU/memory usage

### Slow Frontend Load

**Problem:** Frontend takes > 3s to load

**Solutions:**
1. Run production build:
   ```bash
   npm run build
   npm run preview
   ```
2. Check network tab in DevTools
3. Enable gzip compression
4. Optimize images
5. Use CDN for static assets

### Vision Analysis Too Slow

**Problem:** Image analysis takes > 2s

**Solutions:**
1. Resize large images before upload
2. Use GPU if available
3. Optimize MediaPipe models
4. Check CPU temperature (may be throttling)

## Memory Issues

### Out of Memory (Backend)

**Error:** `MemoryError` or process killed

**Solutions:**
1. Reduce image batch size
2. Clear cache periodically
3. Increase available memory
4. Process images one at a time

### High Memory Usage (Frontend)

**Problem:** Browser memory usage high

**Solutions:**
1. Clear browser cache
2. Optimize React components
3. Remove unused dependencies
4. Use React.memo() for expensive components

## API Issues

### 404 Not Found

**Error:** `404 Not Found` on API calls

**Solutions:**
1. Verify API URL is correct
2. Check backend is running
3. Verify route exists: `/api/...`
4. Check HTTP method (GET, POST, etc.)

### 500 Internal Server Error

**Error:** `500 Internal Server Error`

**Solutions:**
1. Check backend logs
2. Verify input data is valid
3. Check database connectivity (if applicable)
4. Verify all dependencies are installed

### 429 Too Many Requests

**Error:** `429 Too Many Requests`

**Solution:** Rate limiting is in place. Wait before retrying.

## Browser Issues

### WebGL Not Supported

**Error:** WebGL errors in console

**Solution:** Use a modern browser that supports WebGL

### HTTPS Mixed Content

**Error:** `Blocked by client-side security restrictions`

**Solution:** Use HTTPS in production

## Getting Help

If your issue isn't listed:

1. Check [GitHub Issues](https://github.com/PhantomX-stack/ai-personal-stylist-vton/issues)
2. Search the [Wiki](https://github.com/PhantomX-stack/ai-personal-stylist-vton/wiki)
3. Ask in [Discussions](https://github.com/PhantomX-stack/ai-personal-stylist-vton/discussions)
4. Check backend/frontend logs for error details
5. Enable debug mode if available

---

**Last Updated:** 2026-03-06
