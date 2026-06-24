# models/ollama_client.py

import requests

from config.settings import (
    OLLAMA_BASE_URL,
    MODEL_NAME,
    TEMPERATURE,
    TOP_P
)


def generate_response(prompt):
    """
    Generate response using local Ollama model.
    """

    try:

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": TEMPERATURE,
                "top_p": TOP_P
            }
        }

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "No response generated."
        )

    except requests.exceptions.ConnectionError:

        return (
            "Unable to connect to Ollama.\n"
            "Please ensure Ollama is running."
        )

    except Exception as e:

        return f"Error: {str(e)}"