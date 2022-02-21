import pytest

from app import app

@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    response = client.get('/')
    html = response.data.decode()
    assert response.status_code == 200
    assert "Name. first event" in html
    assert "Name. second event" in html
    assert "Name. third event" in html
    assert "Price. 10.0" in html
    assert "Price. 5.0" in html


def test_submit_first_event(client):
    response = client.post("/submit_event", data={
        "event": 'first event'
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert "Product. apple" in html
    assert "Product. banana" in html
    assert "Product. strawberry" in html
    assert "Price. 10.0" in html
    assert "Price. 5.0" in html


def test_submit_products_first(client):
    response = client.post("/submit_products", data={
        "price": '10'
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert "Total service fee 20.0" in html


def test_submit_second_event(client):
    response = client.post("/submit_event", data={
        "event": 'second event'
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert "Product. apple" in html
    assert "Product. banana" in html
    assert "Product. strawberry" in html
    assert "Product. lemon" in html
    assert "Price. 10.0" in html
    assert "Price. 5.0" in html


def test_submit_third_event(client):
    response = client.post("/submit_event", data={
        "event": 'third event'
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert "Product. strawberry" in html
    assert "Product. lemon" in html
    assert "Price. 5.0" in html


def test_submit_products_third(client):
    response = client.post("/submit_products", data={
        "price": '5'
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert "Total service fee 10.0" in html

