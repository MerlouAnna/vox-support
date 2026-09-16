from fastapi.testclient import TestClient

from vox.core.config import Settings
from vox.main import create_app


def test_health_returns_ok(client: TestClient):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_are_hidden_in_production():
    app = create_app(Settings(_env_file=None, environment="production"))
    app.docs_url is None
