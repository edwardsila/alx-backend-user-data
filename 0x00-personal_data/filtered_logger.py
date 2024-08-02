#!/usr/bin/env python3
"""
   returns log message obfuscated
"""

import re


def filter_datum(
        fields: str,
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    pattern = f"({'|'.join([f'{field}=[^{separator}]+' for field in fields])})"
    return re.sub(
            pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}",
            message)
