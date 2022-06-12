from peewee import (
    CompositeKey,
    DecimalField,
    IntegerField,
    TextField,
    SQL,
)
from playhouse.postgres_ext import DateTimeTZField

from app.models.base import BaseModel


class DeviceReading(BaseModel):
    barometric = DecimalField(null=True)
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
