"""
Utility functions used across the ETL pipeline.
"""

import os
import logging


# -----------------------------
# Logger Setup
# -----------------------------
def get_logger(name: str):
    """Create and return a formatted logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# -----------------------------
# Directory Helpers
# -----------------------------
def ensure_dir(path: str):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False


# -----------------------------
# File Helpers
# -----------------------------
def file_exists(path: str) -> bool:
    """Check if a file exists."""
    return os.path.isfile(path)
