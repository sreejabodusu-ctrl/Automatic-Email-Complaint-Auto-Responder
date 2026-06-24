# app.py

import streamlit as st

from pages.dashboard import show_dashboard
from pages.complaint_analysis import show_complaint_analysis
from pages.complaint_history import show_complaint_history
from pages.settings import show_settings

from config.settings import (
    APP_NAME,
    APP_VERSION,
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE
)

# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)

# --------------------------------
# Custom CSS
# --------------------------------

st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: bold;
    color: #1f77b4;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------
# Header
# --------------------------------

st.markdown(
    f'<p class="main-title">{APP_NAME}</p>',
    unsafe_allow_html=True
)

st.caption(
    "AI-Powered Customer Complaint Auto-Responder using Ollama + Llama 3"
)

# --------------------------------
# Sidebar
# --------------------------------

with st.sidebar:

    st.title("📂 Navigation")

    page = st.radio(
        "Choose a page",
        [
            "Dashboard",
            "Complaint Analysis",
            "Complaint History",
            "Settings"
        ]
    )

    st.divider()

    st.subheader("Application Info")

    st.write(f"Version: {APP_VERSION}")
    st.write("Model: Llama 3")
    st.write("Backend: Ollama")

    st.divider()

    st.info(
        "This application automatically "
        "analyzes customer complaints and "
        "generates professional email responses."
    )

# --------------------------------
# Page Routing
# --------------------------------

try:

    if page == "Dashboard":
        show_dashboard()

    elif page == "Complaint Analysis":
        show_complaint_analysis()

    elif page == "Complaint History":
        show_complaint_history()

    elif page == "Settings":
        show_settings()

except Exception as e:

    st.error(
        f"An unexpected error occurred:\n\n{str(e)}"
    )

# --------------------------------
# Footer
# --------------------------------

st.markdown("---")

st.markdown(
    f"""
    <div class="footer">
        {APP_NAME} | Version {APP_VERSION}
    </div>
    """,
    unsafe_allow_html=True
)