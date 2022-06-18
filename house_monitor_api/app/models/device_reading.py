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
    pressure_hpa = DecimalField(null=True)
    humidity_percent = DecimalField(null=True)
    id = IntegerField(index=True, constraints=[SQL("DEFAULT nextval('device_readings_id_seq'::regclass)")])
    device_id = TextField()
    reading_ts = DateTimeTZField(index=True)
    temperature_c = DecimalField(null=True)

    class Meta:
        table_name = 'device_readings'
        indexes = (
            (('reading_ts', 'device_id', 'id'), True),
        )
        primary_key = CompositeKey('reading_ts', 'device_id', 'id')
