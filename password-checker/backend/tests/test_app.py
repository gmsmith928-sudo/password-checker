import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_basic(client):
    r = client.post('/api/check', json={"password":"Test123!"})
    assert r.status_code == 200
