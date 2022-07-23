import falcon

from app import config
from app.models.base import DATABASE


class Healthcheck:
    def on_get(self, request: falcon.Request, response: falcon.Response) -> None:
        DATABASE.execute_sql('SELECT false;')

        response.context.content = {
            'version': config.VERSION,
            'database_status': 'healthy', # TODO
        }
