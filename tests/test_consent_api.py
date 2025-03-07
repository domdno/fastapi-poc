# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Dict, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.patch_patient_consents_brand200_response import PatchPatientConsentsBrand200Response  # noqa: F401
from openapi_server.models.patch_patient_consents_brand_request import PatchPatientConsentsBrandRequest  # noqa: F401


def test_patch_patient_consents_brand(client: TestClient):
    """Test case for patch_patient_consents_brand

    Update Consents and Preferences
    """
    patch_patient_consents_brand_request = {"consentsAndPreferences":[{"name":"cyltezoPatientNavigator","status":"optIn"},{"name":"cyltezoCopayTextMessageCommunications","status":"optOut"}],"dataProviderId":"CMMH","dataProviderTransactionId":"2398329334","dataProviderPatientId":"10000045678"}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/patients/{id}/consents".format(id='id_example'),
    #    headers=headers,
    #    json=patch_patient_consents_brand_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

