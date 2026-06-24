# services/export_service.py

import os
import pandas as pd
from datetime import datetime

from config.settings import (
    COMPLAINT_HISTORY_FILE
)


def save_to_history(
    complaint,
    category,
    priority,
    response
):
    """
    Save complaint information.
    """

    record = {
        "timestamp": datetime.now(),
        "complaint": complaint,
        "category": category,
        "priority": priority,
        "response": response
    }

    df = pd.DataFrame([record])

    file_exists = os.path.exists(
        COMPLAINT_HISTORY_FILE
    )

    df.to_csv(
        COMPLAINT_HISTORY_FILE,
        mode="a",
        header=not file_exists,
        index=False
    )


def load_history():
    """
    Load complaint history.
    """

    try:

        return pd.read_csv(
            COMPLAINT_HISTORY_FILE
        )

    except FileNotFoundError:

        return pd.DataFrame()


def export_csv(
    dataframe,
    filename
):
    """
    Export dataframe to CSV.
    """

    dataframe.to_csv(
        filename,
        index=False
    )

    return filename