# services/response_generator.py

from models.ollama_client import (
    generate_response
)

from config.settings import (
    PROMPT_TEMPLATE,
    DEFAULT_TONE
)


def create_email_response(
    complaint,
    category,
    tone=DEFAULT_TONE
):
    """
    Generate customer support reply.
    """

    prompt = PROMPT_TEMPLATE.format(
        category=category,
        tone=tone,
        complaint=complaint
    )

    response = generate_response(
        prompt
    )

    return response