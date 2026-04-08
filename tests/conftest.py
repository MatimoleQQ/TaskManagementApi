import pytest
from fastapi.testclient import TestClient
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.main import app

# Tworzenie bazy testowej
@pytest.fixture(scope="module")
def test_db():
    # Usuń istniejące tabele
    Base.metadata.drop_all(bind=engine)
    # Utwórz wszystkie tabele na nowo
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

# Klient testowy FastAPI
@pytest.fixture(scope="module")
def client():
    return TestClient(app)