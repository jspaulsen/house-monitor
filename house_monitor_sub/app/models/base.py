from contextlib import contextmanager

from peewee import Model
from playhouse.pool import PooledPostgresqlDatabase

from app import config


DATABASE = PooledPostgresqlDatabase(
    config.DATABASE_URL,
    autorollback=True,
)


class BaseModel(Model):
    class Meta:
        database = DATABASE


@contextmanager
def db_connection():
    try:
        yield DATABASE.connect(reuse_if_open=True)
    finally:
        DATABASE.close()
