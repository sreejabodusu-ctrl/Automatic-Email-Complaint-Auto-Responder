# models/complaint_classifier.py

from config.settings import COMPLAINT_CATEGORIES


def classify_complaint(complaint_text):
    """
    Detect complaint category using keywords.
    """

    complaint_text = complaint_text.lower()

    for keyword, category in COMPLAINT_CATEGORIES.items():
        if keyword in complaint_text:
            return category

    return "General Complaint"


def get_priority(complaint_text):
    """
    Assign complaint priority.
    """

    complaint_text = complaint_text.lower()

    high_priority_words = [
        "urgent",
        "fraud",
        "scam",
        "legal",
        "complaint",
        "cancel",
        "lost",
        "damaged"
    ]

    for word in high_priority_words:
        if word in complaint_text:
            return "High"

    return "Normal"