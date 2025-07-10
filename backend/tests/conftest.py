import pytest
from fastapi.testclient import TestClient
import alembic.config
from app.main import app

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    alembic.config.main(["--config", "backend/alembic.ini", "upgrade", "head"])
    yield

@pytest.fixture
def client():
    return TestClient(app)
