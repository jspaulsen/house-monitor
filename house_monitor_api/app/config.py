from __future__ import annotations
import os


DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')


def missing() -> list[str]:
    pass
