import os

import pytest

from app.models.base import DATABASE


SKIP_DATABASE_TESTS = os.getenv('SKIP_DATABASE_TESTS', 'true').lower() in ['true', 'yes', '1']

database_required = pytest.mark.skipif(SKIP_DATABASE_TESTS, reason="Only run database tests if enabled")


@pytest.fixture
def mock_db_connection(mocker):
    mocker.patch.object(
        DATABASE,
        'connect',
    )

    mocker.patch.object(
        DATABASE,
        'close',
    )
