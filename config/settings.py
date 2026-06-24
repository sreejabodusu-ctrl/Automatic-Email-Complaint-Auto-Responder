# config/settings.py

import os
from pathlib import Path

# ==========================
# PROJECT PATHS
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"
EXPORTS_DIR = REPORTS_DIR / "exports"
RESPONSES_DIR = REPORTS_DIR / "generated_responses"

ASSETS_DIR = BASE_DIR / "assets"

# Create folders if they don't exist
for folder in [
    DATA_DIR,
    REPORTS_DIR,
    EXPORTS_DIR,
    RESPONSES_DIR
]:
    folder.mkdir(parents=True, exist_ok=True)

# ==========================
# OLLAMA CONFIGURATION
# ==========================

OLLAMA_BASE_URL = "http://localhost:11434"

# Installed model name
MODEL_NAME = "llama3"

# Generation parameters
TEMPERATURE = 0.7
TOP_P = 0.9
MAX_TOKENS = 500

# ==========================
# APPLICATION SETTINGS
# ==========================

APP_NAME = "Automatic Email Complaint Auto-Responder"

APP_VERSION = "1.0.0"

DEFAULT_LANGUAGE = "English"

ENABLE_HISTORY = True

ENABLE_EXPORTS = True

# ==========================
# FILES
# ==========================

COMPLAINT_HISTORY_FILE = (
    DATA_DIR / "complaint_history.csv"
)

COMPLAINT_DATASET_FILE = (
    DATA_DIR / "complaints.csv"
)

# ==========================
# COMPLAINT CATEGORIES
# ==========================

COMPLAINT_CATEGORIES = {
    "delivery": "Shipping Issue",
    "shipping": "Shipping Issue",
    "refund": "Refund Request",
    "return": "Refund Request",
    "damaged": "Damaged Product",
    "broken": "Damaged Product",
    "payment": "Payment Issue",
    "billing": "Payment Issue",
    "invoice": "Payment Issue",
    "account": "Account Issue",
    "login": "Account Issue",
}

# ==========================
# RESPONSE TONES
# ==========================

AVAILABLE_TONES = [
    "Professional",
    "Friendly",
    "Formal",
    "Empathetic"
]

DEFAULT_TONE = "Professional"

# ==========================
# STREAMLIT SETTINGS
# ==========================

PAGE_TITLE = APP_NAME

PAGE_ICON = "📧"

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

# ==========================
# LOGGING
# ==========================

LOG_FILE = BASE_DIR / "app.log"

LOG_LEVEL = "INFO"

# ==========================
# PROMPT TEMPLATE
# ==========================

PROMPT_TEMPLATE = """
You are an experienced customer support representative.

Complaint Category:
{category}

Response Tone:
{tone}

Customer Complaint:
{complaint}

Instructions:
1. Be polite and professional.
2. Apologize if necessary.
3. Provide helpful guidance.
4. Keep response concise.
5. End with a professional closing.

Generate the email response:
"""