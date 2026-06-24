# pages/complaint_analysis.py

import streamlit as st

from services.category_service import (
    analyze_complaint
)

from services.response_generator import (
    create_email_response
)

from services.export_service import (
    save_to_history
)

from config.settings import (
    AVAILABLE_TONES
)


def show_complaint_analysis():

    st.title(
        "📧 Complaint Analysis"
    )

    complaint = st.text_area(
        "Enter Customer Complaint",
        height=200
    )

    tone = st.selectbox(
        "Response Tone",
        AVAILABLE_TONES
    )

    if st.button(
        "Generate Response"
    ):

        if not complaint.strip():

            st.warning(
                "Please enter a complaint."
            )

            return

        with st.spinner(
            "Analyzing complaint..."
        ):

            result = analyze_complaint(
                complaint
            )

            category = result["category"]
            priority = result["priority"]

            response = create_email_response(
                complaint,
                category,
                tone
            )

            save_to_history(
                complaint,
                category,
                priority,
                response
            )

            st.success(
                "Response Generated"
            )

            st.subheader(
                "Complaint Details"
            )

            st.write(
                f"**Category:** {category}"
            )

            st.write(
                f"**Priority:** {priority}"
            )

            st.subheader(
                "Generated Response"
            )

            st.text_area(
                "",
                response,
                height=250
            )