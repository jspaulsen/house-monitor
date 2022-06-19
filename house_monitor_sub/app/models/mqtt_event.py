from decimal import Decimal
from typing import Optional

import pydantic

from app.models.iso8601dt import ISO8601DateTime


class BME280(pydantic.BaseModel):
    temperature: Decimal = pydantic.Field(alias='Temperature')
    humidity: Decimal = pydantic.Field(alias='Humidity')
    pressure: Decimal = pydantic.Field(alias='Pressure')


class MQTTEvent(pydantic.BaseModel):
    class Config:
        extra = pydantic.Extra.allow
    
    time: ISO8601DateTime = pydantic.Field(alias='Time')

    # Potential field(s) which vary based on source
    bme: Optional[BME280] = pydantic.Field(default=None, alias='BME280')
