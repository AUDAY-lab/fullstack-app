# Full-Stack App

A full-stack application with Node.js frontend and Flask backend.

## Features
- A form with Name and Email fields
- Node.js/Express frontend
- Flask backend with MongoDB
- Docker containerized

## Project Structure
```
fullstack-app/
├── docker-compose.yml
├── .gitignore
├── README.md
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── server.js
│   └── views/
│       └── index.ejs
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

## Quick Start

1. **Clone and setup:**
   ```bash
   mkdir fullstack-app
   cd fullstack-app
   # Copy all files to respective directories
   ```

2. **Run with Docker:**
   ```bash
   docker-compose up --build
   ```

3. **Access:**
   - Frontend: http://localhost:3000
   - Backend: http://localhost:5000

## API Endpoints
- `GET /` - Backend health check
- `POST /submit` - Submit form data
- `GET /users` - Get all users (for checking backend)

## Docker Hub
```bash
# Build images
docker build -t audaylab/fullstack-frontend ./frontend
docker build -t audaylab/fullstack-backend ./backend

# Push to Docker Hub
docker push audaylab/fullstack-frontend
docker push audaylab/fullstack-backend
```

## View Data
Check backend logs to see submitted data:
```bash
docker-compose logs backend
```