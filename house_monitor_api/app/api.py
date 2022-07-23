import falcon

from app.middleware.authorization import AuthorizationMiddleware
from app.middleware.connection import DatabaseConnection
from app.middleware.json import JsonMiddleware
from app.resources.device_reading import DeviceReading
from app.resources.healthcheck import Healthcheck


class API(falcon.App):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            middleware=[
                AuthorizationMiddleware(),
                DatabaseConnection(),
                JsonMiddleware(),
            ],
            **kwargs,
        )

        self.add_route('/health-check', Healthcheck())
        
        self.add_route('/v1/readings', DeviceReading())
