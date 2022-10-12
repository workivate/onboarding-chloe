from chocs import HttpStatus
from chocs.testing import TestClient


def test_get_status_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/status")

    assert response.status_code == HttpStatus.OK  # nosec B101


def test_options_status_endpoint(test_client: TestClient) -> None:
    response = test_client.options("/status")

    assert response.status_code == HttpStatus.OK  # nosec B101
    assert response.headers["content-type"] == "application/json"  # nosec B101
    assert response.headers["access-control-allow-origin"] == "*"  # nosec B101
    assert response.headers["access-control-allow-credentials"] == "true"  # nosec B101
    assert (  # nosec B101
        response.headers["access-control-allow-headers"] == "accept, Authorization"
    )
    assert (  # nosec B101
        response.headers["access-control-allow-methods"] == "OPTIONS, GET"
    )

    assert "x-request-id" in response.headers  # nosec B101
    assert "x-causation-id" in response.headers  # nosec B101
    assert "x-correlation-id" in response.headers  # nosec B101


def test_get_ping_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/ping")

    assert response.status_code == HttpStatus.NO_CONTENT  # nosec B101
