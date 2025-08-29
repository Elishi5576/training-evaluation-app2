
# Training Evaluation App

This is a Flask-based web application for evaluating employee training performance.

## Features
- Input employee names and scores for 8 training categories
- Generate radar chart and Excel report
- Web-based form interface

## Deployment on Render

1. Upload this repository to GitHub
2. Go to [Render](https://render.com) and create a new Web Service
3. Set the following parameters:
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Your app will be deployed at `https://your-app-name.onrender.com`

## Required Files
- `requirements.txt`
- `app.py`
- `templates/form.html`
- `templates/evaluate.html`
- `static/` folder for output files
