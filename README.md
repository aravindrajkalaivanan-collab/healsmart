# 🏥 Anu Multi-Specialty Hospital & Research Center (HealSmart)

An integrated digital health ecosystem with:
- **Instant Doctor Clinical Response & Treatment Solver**
- **Multi-Department Specialist Roster (9 Departments)**
- **Chief Doctor Case Allocation & Triage Hub**
- **Persistent SQLite Database (`healsmart.db`)**
- **Live Hospital Footfall & Traffic Analytics**
- **Patient Reviews & Star Rating System**
- **Google SEO & Schema.org Medical Data**

---

## 💻 How to Run in VS Code

### 1. Open in VS Code
1. Open VS Code.
2. Click **File** ➔ **Open Folder...**
3. Select this folder: `C:\Users\DELL\.gemini\antigravity\scratch\healsmart`

### 2. Install Dependencies
Open the VS Code Terminal (`Ctrl + \`` or **Terminal** ➔ **New Terminal**):
```bash
pip install -r requirements.txt
```

### 3. Run the Platform
```bash
python run.py
```
Open your browser at: **http://127.0.0.1:8000**

---

## 🌐 How to Publish Online (100% Free on Render.com)

1. Push this folder to a new repository on [GitHub.com](https://github.com).
2. Go to [Render.com](https://render.com) ➔ **New Web Service**.
3. Select your GitHub repository.
4. Settings:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Click **Create Web Service** to get your public HTTPS URL!
