# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.get_healthcheck200_response import GetHealthcheck200Response  # noqa: F401


def test_get_healthcheck(client: TestClient):
    """Test case for get_healthcheck

    Healthcheck
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/healthcheck",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

