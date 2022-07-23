import os

from falcon import testing
import pytest

from app.api import API
from app.models.base import DATABASE


SKIP_DATABASE_TESTS = os.getenv('SKIP_DATABASE_TESTS', 'true').lower() in ['true', 'yes', '1']

database_required = pytest.mark.skipif(SKIP_DATABASE_TESTS, reason="Only run database tests if enabled")


@pytest.fixture
def api() -> API:
    return API()


@pytest.fixture
def authed_client(mock_authorization, api):
    return testing.TestClient(api)


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


@pytest.fixture
def mock_authorization(mocker):
    class AuthMiddlewareMock:
        def process_request(self, *_, **__) -> None:
            pass
    
    yield mocker.patch('app.api.AuthorizationMiddleware', return_value=AuthMiddlewareMock())
