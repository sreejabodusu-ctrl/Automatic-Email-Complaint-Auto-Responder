# services/category_service.py

from models.complaint_classifier import (
    classify_complaint,
    get_priority
)


def analyze_complaint(complaint_text):
    """
    Analyze complaint and return
    category + priority.
    """

    category = classify_complaint(
        complaint_text
    )

    priority = get_priority(
        complaint_text
    )

    return {
        "category": category,
        "priority": priority
    }