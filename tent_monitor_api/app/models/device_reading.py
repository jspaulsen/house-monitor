from peewee import (
    AutoField,
    CompositeKey,
    DecimalField,
    TextField,
    SQL,
)
from playhouse.postgres_ext import DateTimeTZField

from app.models.base import BaseModel


class DeviceReading(BaseModel):
    barometric = DecimalField(null=True)
    device_id = TextField()
    humidity = DecimalField(null=True)
    id = AutoField(constraints=[SQL("DEFAULT nextval('device_readings_id_seq'::regclass)")])
    reading_ts = DateTimeTZField(index=True)
    temperature = DecimalField(null=True)

    class Meta:
        table_name = 'device_readings'
        indexes = (
            (('reading_ts', 'device_id', 'id'), True),
        )
        primary_key = CompositeKey('reading_ts', 'device_id', 'id')
