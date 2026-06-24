# pages/settings.py

import streamlit as st

from config.settings import (
    MODEL_NAME,
    OLLAMA_BASE_URL,
    DEFAULT_TONE,
    APP_VERSION
)


def show_settings():

    st.title("⚙ Settings")

    st.subheader(
        "Application Information"
    )

    st.write(
        f"**Version:** {APP_VERSION}"
    )

    st.write(
        f"**Model:** {MODEL_NAME}"
    )

    st.write(
        f"**Ollama URL:** "
        f"{OLLAMA_BASE_URL}"
    )

    st.write(
        f"**Default Tone:** "
        f"{DEFAULT_TONE}"
    )

    st.success(
        "Configuration loaded successfully."
    )