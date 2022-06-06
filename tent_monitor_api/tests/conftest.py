import os

import pytest

from app.api import API


SKIP_DATABASE_TESTS = os.getenv('SKIP_DATABASE_TESTS', 'true').lower() in ['true', 'yes', '1']

database_required = pytest.mark.skipif(SKIP_DATABASE_TESTS)


@pytest.fixture
def api() -> API:
    return API()




