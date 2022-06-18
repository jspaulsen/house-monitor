import os
from pathlib import Path


DATABASE_URL = os.getenv('DATABASE_URL')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
MQTT_BROKER_HOST = os.getenv('MQTT_BROKER_HOST')
MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', '1883'))
VERSION = (Path(__file__).parents[1] / 'VERSION').open().read().strip()

REQUIRED_ENV_VAR = [
    'DATABASE_URL',
    'MQTT_BROKER_HOST',
]


def missing_configuration() -> list[str]:
    return [
        env for env in REQUIRED_ENV_VAR if
        os.getenv(env) is None
    ]
