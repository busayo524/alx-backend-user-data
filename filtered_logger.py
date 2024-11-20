#!/usr/bin/env python3
"""A module for filtering logs using regex."""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Filters sensitive information from a log message.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): Replacement text for obfuscated values.
        message (str): Input log message.
        separator (str): Field separator in the log message.

    Returns:
        str: The log message with sensitive fields redacted.
    """
    pattern = r"({})=[^{}]*".format("|".join(fields), separator)
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
