from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from vox.core.config import Settings
from vox.main import create_app


@pytest.fixture
def client() -> Iterator[TestClient]:
    settings = Settings(_env_file=None, environment="local")
    app = create_app(settings=settings)
    with (
        TestClient(app) as test_client
    ):  # this is a context mnanager - entering it runs __enter__ and exiting runs __exit__
        yield test_client
