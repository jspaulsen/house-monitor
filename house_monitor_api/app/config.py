import os
from pathlib import Path


DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

VERSION = (Path(__file__).parents[1] / 'VERSION').open().read().strip()
