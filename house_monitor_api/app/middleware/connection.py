import re
from app.models.base import DATABASE


class DatabaseConnection:
    def process_request(self, *_, **__) -> None:
        DATABASE.connect(reuse_if_open=True)

    def process_response(self, *_, **__) -> None:
        DATABASE.close()
