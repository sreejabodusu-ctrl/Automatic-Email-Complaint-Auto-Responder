# pages/complaint_history.py

import streamlit as st

from services.export_service import (
    load_history
)


def show_complaint_history():

    st.title(
        "📜 Complaint History"
    )

    history = load_history()

    if history.empty:

        st.info(
            "No complaint history available."
        )

        return

    st.dataframe(
        history,
        use_container_width=True
    )

    csv_data = (
        history.to_csv(
            index=False
        ).encode("utf-8")
    )

    st.download_button(
        label="⬇ Download CSV",
        data=csv_data,
        file_name="complaint_history.csv",
        mime="text/csv"
    )