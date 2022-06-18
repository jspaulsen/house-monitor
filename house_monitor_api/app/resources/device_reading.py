import falcon

from app.hooks.validate import validate_json
from app.models.device_reading import DeviceReading
from app.schemas.device_reading import DeviceReadingSchema


class DeviceReading:
    @validate_json(DeviceReadingSchema)
    def on_post(self, request: falcon.Request) -> None:
        pass


    # barometric = DecimalField(null=True)
    # humidity = DecimalField(null=True)
    # id = IntegerField(index=True, constraints=[SQL("DEFAULT nextval('device_readings_id_seq'::regclass)")])
    # device_id = TextField()
    # reading_ts = DateTimeTZField(index=True)
    # temperature = DecimalField(null=True)
