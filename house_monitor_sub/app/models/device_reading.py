from __future__ import annotations

from peewee import (
    CompositeKey,
    DecimalField,
    IntegerField,
    ModelInsert,
    TextField,
    SQL,
)
from playhouse.postgres_ext import DateTimeTZField

from app.models.base import BaseModel
from app.models.mqtt_event import MQTTEvent


class DeviceReading(BaseModel):
    pressure = DecimalField(null=True)
    humidity = DecimalField(null=True)
    id = IntegerField(index=True, constraints=[SQL("DEFAULT nextval('device_readings_id_seq'::regclass)")])
    device_id = TextField()
    reading_ts = DateTimeTZField(index=True)
    temperature = DecimalField(null=True)

    class Meta:
        table_name = 'device_readings'
        indexes = (
            (('reading_ts', 'device_id', 'id'), True),
        )
        primary_key = CompositeKey('reading_ts', 'device_id', 'id')

    @classmethod
    def from_mqtt_event(cls, device_id: str, event: MQTTEvent) -> ModelInsert:
        return cls.insert(
            device_id=device_id,
            reading_ts=event.time,
            **event.bme.dict(),
        )
