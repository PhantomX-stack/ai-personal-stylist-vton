# 🐳 Docker Setup Guide

This guide covers running the AI Personal Stylist application using Docker for both local development and production deployments.

## Prerequisites

- **Docker Desktop** installed ([Download](https://www.docker.com/products/docker-desktop/))
- **Docker Compose** (included with Docker Desktop)
- Git installed

## Quick Start with Docker

### Option 1: Using Docker Compose (Recommended)

The easiest way to run both backend and frontend together:

```bash
# 1. Clone the repository
git clone https://github.com/PhantomX-stack/ai-personal-stylist-vton.git
cd ai-personal-stylist-vton

# 2. Start all services with Docker Compose
docker-compose up --build

# The application will be available at:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

**That's it!** Everything runs in containers.

### Option 2: Individual Docker Containers

If you prefer running containers separately:

#### Start Backend Container

```bash
cd backend
docker build -t ai-stylist-backend .
docker run -p 8000:8000 ai-stylist-backend
```

#### Start Frontend Container (in another terminal)

```bash
cd frontend
docker build -t ai-stylist-frontend .
docker run -p 3000:3000 ai-stylist-frontend
```

## Docker Images

### Backend Image

- **Base Image**: `python:3.9-slim`
- **Port**: 8000
- **Command**: `uvicorn app:app --host 0.0.0.0 --port 8000`
- **Size**: ~2.5GB (includes OpenCV, MediaPipe, ML dependencies)

### Frontend Image

- **Base Image**: `node:18-alpine` (multi-stage build)
- **Port**: 3000
- **Build Tool**: Vite
- **Final Size**: ~200MB (optimized with multi-stage build)

## Docker Compose Services

The `docker-compose.yml` defines two services:

```yaml
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - VITE_API_URL=http://localhost:8000/api
```

## Common Docker Commands

### Build Images

```bash
# Build all services
docker-compose build

# Build specific service
docker-compose build backend
```

### Run Services

```bash
# Run in foreground
docker-compose up

# Run in background
docker-compose up -d

# Build and run
docker-compose up --build
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Stop Services

```bash
# Stop all services
docker-compose stop

# Stop and remove containers
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## Troubleshooting Docker

### Port Already in Use

```bash
# Change ports in docker-compose.yml
# Or kill existing processes
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:3000 | xargs kill -9  # Frontend
```

### Docker Build Fails

```bash
# Clear build cache
docker-compose build --no-cache

# Free up disk space
docker system prune -a
```

### Container Crashes

```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild
docker-compose down -v
docker-compose up --build
```

## Local Development with Docker

For development with hot-reload, mount volumes:

```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

Or modify `docker-compose.yml` to add volume mounts:

```yaml
volumes:
  - ./backend:/app  # Backend code changes reflected
  - ./frontend/src:/app/src  # Frontend code changes reflected
```

## Production Deployment

### Using Render.com

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions on deploying to Render, Heroku, or other platforms.

### Using Docker Hub

```bash
# Build and push to Docker Hub
docker build -t yourusername/ai-stylist-backend ./backend
docker push yourusername/ai-stylist-backend

docker build -t yourusername/ai-stylist-frontend ./frontend
docker push yourusername/ai-stylist-frontend
```

### Environment Variables

Create a `.env` file in the project root:

```bash
# Backend
PYTHON_ENV=production
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com

# Frontend
VITE_API_URL=http://localhost:8000/api
```

## Performance Tips

- **Use `.dockerignore`** to exclude unnecessary files (node_modules, venv, etc.)
- **Multi-stage builds** reduce final image size
- **Layer caching** - put frequently changing code last in Dockerfile
- **Health checks** - add to docker-compose.yml for production

## Alternative: Local Development (No Docker)

If you prefer running locally without Docker, see [QUICK_START.md](./QUICK_START.md).

## Getting Help

- **Docker Logs**: `docker-compose logs -f`
- **API Documentation**: http://localhost:8000/docs
- **Issues**: [Report on GitHub](https://github.com/PhantomX-stack/ai-personal-stylist-vton/issues)
- **Troubleshooting**: See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

---

**Next Steps**: 
1. Run `docker-compose up --build`
2. Open http://localhost:3000 in your browser
3. Start styling with AI!
