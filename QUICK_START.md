# Quick Start Guide - Get Running in 2 Minutes!

⚡ **The absolute fastest way to run AI Personal Stylist locally**

## Prerequisites (Install if you don't have)

- **Python 3.9+**: https://www.python.org/downloads/
- **Node.js 16+**: https://nodejs.org/
- **Git**: https://git-scm.com/

## Step-by-Step (Copy & Paste These Commands)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/PhantomX-stack/ai-personal-stylist-vton.git
cd ai-personal-stylist-vton
```

### 2️⃣ Start Backend (Terminal 1)

```bash
cd backend
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

pip install -r ../requirements.txt
uvicorn app:app --reload
```

✅ **You should see:**
```
Application startup complete
Uvicorn running on http://127.0.0.1:8000
```

**Backend is now running!** Open another terminal for frontend.

### 3️⃣ Start Frontend (Terminal 2)

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

✅ **You should see:**
```
LOCAL:   http://localhost:5173/
```

### 4️⃣ Open Your Browser

**Go to: http://localhost:5173**

🎉 **Your AI Personal Stylist is now running!**

---

## Troubleshooting

### ❌ "Connection refused" error?

**Solution:** Make sure both terminals are still running:
- Terminal 1: Backend (`uvicorn app:app --reload`) should be running
- Terminal 2: Frontend (`npm run dev`) should be running

### ❌ Port 5173 already in use?

```bash
# Use a different port
npm run dev -- --port 3000
# Then visit: http://localhost:3000
```

### ❌ Port 8000 already in use?

```bash
# Use a different port
uvicorn app:app --reload --port 8001
# Update frontend .env:
# VITE_API_URL=http://localhost:8001/api
```

### ❌ Module not found errors?

```bash
# Reinstall dependencies
cd frontend
rm -rf node_modules package-lock.json
npm install

cd backend
pip install --upgrade pip
pip install -r ../requirements.txt
```

### ❌ "python command not found"?

```bash
# Try python3 instead
python3 -m venv venv
source venv/bin/activate
pip3 install -r ../requirements.txt
```

### ❌ npm command not found?

Node.js/npm not installed. Download from: https://nodejs.org/

---

## What Each Terminal Should Show

### Backend Terminal (uvicorn)
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Frontend Terminal (Vite)
```
  ➜  Local:   http://localhost:5173/
  ➜  press h to show help
```

---

## Important Notes

⚠️ **Keep both terminals open!** They need to stay running for the app to work.

⚠️ **Don't close Terminal 1 or Terminal 2** while using the application.

⚠️ **If you get an error in either terminal, the app won't work properly**.

---

## Next Steps

Once it's running:

1. **Upload a photo** to analyze your style
2. **Get recommendations** based on AI analysis
3. **Try virtual try-on** with different clothes
4. **Chat with AI** for fashion advice

---

## Full Documentation

For advanced setup and deployment:
- 📖 [Complete Installation Guide](README.md#-installation-guide)
- 🔧 [Deployment Instructions](DEPLOYMENT.md)
- 🐛 [Troubleshooting](TROUBLESHOOTING.md)
- 🤝 [Contributing](CONTRIBUTING.md)

---

## Still Having Issues?

1. ✅ Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for 30+ solutions
2. 📝 Open an [Issue on GitHub](https://github.com/PhantomX-stack/ai-personal-stylist-vton/issues)
3. 💬 Ask in [GitHub Discussions](https://github.com/PhantomX-stack/ai-personal-stylist-vton/discussions)

---

**Happy styling! 🎨✨**
