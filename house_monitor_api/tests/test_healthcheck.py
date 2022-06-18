from app import config

from .conftest import database_required


class TestHealthcheck:
    @database_required
    def test_health_check(self, authed_client):
        results = authed_client.simulate_get('/health-check')
        
        assert results.status_code == 200
        assert results.json.get('version') == config.VERSION
