# TM3 Global Sovereign Portal

This directory contains static resources and deployment notes for the Flask-based dashboard.

## 🛠 Setup

```bash
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt
```

### 🧪 Run Locally

```bash
python app.py
```

### 🚀 Deployment Instructions

When deploying (e.g., on Render):

- **Build**: `pip install -r requirements.txt`
- **Start**: `gunicorn app:app`
- **Health Check**: `/healthz`

---

## Next Steps
1. **Create these files** in your repo's root.
2. **Commit & push** changes.
3. **Deploy to Render** using the provided configuration.
4. We'll verify your live URL together.

