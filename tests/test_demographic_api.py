# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Dict, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.put_patient_request import PutPatientRequest  # noqa: F401


def test_put_patient(client: TestClient):
    """Test case for put_patient

    Update Patient's demographic
    """
    put_patient_request = {"dataProviderId":"CMMH","dataProviderPatientId":"CMM83475324850","dataProviderTransactionId":"349824842834928374","firstName":"Joshua","lastName":"Baker","birthDate":"1984-02-28","addressLine1":"1874 Massachusetts Avenue","addressLine2":"Apt-100","city":"Lexington","stateOrProvinceCode":"MA","countryCode":"US","postalCode":"02420-5303","communications":[{"type":"homePhone","number":"7818626087"},{"type":"email","address":"patientJoshua@example.com"}],"alternateContact":{"fullName":"Sarah Baker","relationshipToPatient":"spouse"}}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/patients/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=put_patient_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

