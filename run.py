import sys
import os
import uvicorn

# Set current directory to backend
backend_dir = os.path.join(os.path.dirname(__file__), "backend")
sys.path.insert(0, backend_dir)

if __name__ == "__main__":
    print("=" * 60)
    print("Starting Anu Multi-Specialty Hospital - HealSmart Platform")
    print("Local Web App: http://127.0.0.1:8000")
    print("API Documentation: http://127.0.0.1:8000/docs")
    print("=" * 60)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True, app_dir=backend_dir)