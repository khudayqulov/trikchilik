from fastapi.testclient import TestClient

from app.web import create_app


def test_health_endpoint() -> None:
    response = TestClient(create_app()).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_catalog_is_empty_until_products_are_configured() -> None:
    response = TestClient(create_app()).get("/api/products")

    assert response.status_code == 200
    assert response.json() == []


def test_root_serves_the_mini_app() -> None:
    response = TestClient(create_app()).get("/")

    assert response.status_code == 200
    assert "Tirikchilik" in response.text

