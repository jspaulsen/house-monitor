from __future__ import annotations
import logging
import platform

import orjson
from paho.mqtt import client as mqtt_client
import pydantic

from app import config
from app.models.base import db_connection
from app.models.device_reading import DeviceReading
from app.models.mqtt_event import MQTTEvent


MQTT_TOPIC = "tele/+/SENSOR"
MQTT_ERROR_CODES = [
    "Connection Successful",
    "Incorrect Protocol Version",
    "Invalid Client Identifier",
    "Server Unavailable",
    "Bad Username or Password",
    "Not Authorized",
]

logger = logging.getLogger(__name__)


class MQTTConnectionException(Exception):
    """
    Represents an exception thrown by an error when connecting to the 
    MQTT broker
    """
    def __init__(self, error_code: int, *args, **kwargs) -> None:
        try:
            message = MQTT_ERROR_CODES[error_code]
        except IndexError:
            message = f"Unknown Error Code {error_code}"
        
        super().__init__(message, *args, **kwargs)


class MQTTClient:
    def __init__(self, client_id: str | None = None) -> None:
        self.client_id = client_id or f"house-monitor-sub-{platform.node()}"

        # Setup client
        self.client = mqtt_client.Client(client_id=self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

    def connect(self) -> MQTTClient:
        self.client.connect(
            config.MQTT_BROKER_HOST,
            config.MQTT_BROKER_PORT,
        )

        return self
    
    def loop_forever(self) -> None:
        self.client.loop_forever()

    def on_connect(self, _client, _userdata, _flags, rc):
        if rc > 0:
            raise MQTTConnectionException(rc)
        
        logger.info(f"Successful subscription to {config.MQTT_BROKER_HOST}:{config.MQTT_BROKER_PORT}")

        # Subscribe to topic on connection
        self.client.subscribe(MQTT_TOPIC)
    
    def on_message(self, _client, _userdata, msg) -> None:
        payload = msg.payload.decode()

        try:
            event = MQTTEvent(**orjson.loads(payload))
        except (orjson.JSONDecodeError, pydantic.ValidationError) as err:
            logger.warning(f"Failed to parse message from topic {MQTT_TOPIC}: {str(err)}")
            return

        logger.debug(f"Received payload {event} from {msg.topic}")

        if not event.bme:
            logger.debug(f"Unsupported sensor reading from topic {msg.topic}")
            return

        insert = DeviceReading.from_mqtt_event(
            device_id(msg.topic),
            event,
        )

        logging.debug(f"Received reading {event.bme} from topic {msg.topic}")

        with db_connection() as _:
            insert.execute()

    def on_subscribe(self, *_, **__) -> None:
        logger.info(f"Successful connection to topic {MQTT_TOPIC}")


def device_id(topic: str) -> str | None:
    try:
        return topic.split('/')[1]
    except IndexError:
        return None
