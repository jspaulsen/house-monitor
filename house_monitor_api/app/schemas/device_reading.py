from decimal import Decimal

import pydantic

from app.schemas.datetime import ISO8601DateTime


class DeviceReadingSchema(pydantic.BaseModel):
    pressure_hpa: Decimal
    humidity_percent: Decimal
    temperature_c: Decimal
    device_id: str
    reading_ts: ISO8601DateTime
