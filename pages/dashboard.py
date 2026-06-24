# pages/dashboard.py

import streamlit as st
import pandas as pd

from services.export_service import load_history


def show_dashboard():

    st.title("📊 Dashboard")

    history = load_history()

    if history.empty:
        st.info("No complaints available yet.")
        return

    total_complaints = len(history)

    shipping_count = len(
        history[
            history["category"] == "Shipping Issue"
        ]
    )

    refund_count = len(
        history[
            history["category"] == "Refund Request"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Complaints",
            total_complaints
        )

    with col2:
        st.metric(
            "Shipping Issues",
            shipping_count
        )

    with col3:
        st.metric(
            "Refund Requests",
            refund_count
        )

    st.subheader("Recent Complaints")

    st.dataframe(
        history.tail(10),
        use_container_width=True
    )