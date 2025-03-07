# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.patch_patients_id_services_brand_request import PatchPatientsIdServicesBrandRequest  # noqa: F401


def test_patch_patients_id_services_brand(client: TestClient):
    """Test case for patch_patients_id_services_brand

    Update Patient Services
    """
    patch_patients_id_services_brand_request = {"dataProviderId":"CMMH","dataProviderPatientId":"CMM83475324850","dataProviderTransactionId":"959587457643569846984","clinicalDetails":{"prescription":{"drugName":"zongertinib","drugGroup":"TKI","medicationTier":"tier one"}},"insuranceTypes":["commertial"],"insurancePlans":[{"planType":"pharmacy","planName":"familyhealth01","rxBin":"123456","rxPcn":"12345678910","groupNumber":"OCJ3048","memberId":"379847593745","provider":"CVS","providerPhoneNumber":"1-800-872-3862","policyholderName":"Josh Baker","policyholderBirthDate":"1984-02-28","insuranceHierarchy":"primary","coinsurancePercentage":"80 percent"}],"serviceSubscriptions":[{"serviceType":"caseManagement","subscriptionStatus":"optIn","caseId":"CMMCASEKEY123048","patientJourneyStatus":"3rd Party Restriction","benefitsVerificationStatus":"Benefit Investigation completed","priorAuthorizationStatus":"required","priorAuthorizationRequired":"yes","priorAuthorizationExpiredDate":"2025-08-24T14:15:22Z","priorAuthorizationId":"8320204"},{"serviceType":"rxBridge","subscriptionStatus":"optIn","subscriptionDate":"2019-08-24","bridgeStatus":"Shipped","triageDate":"2025-08-24T14:15:22Z","prescription":{"drugName":"zongertinib","status":"string","shippedDate":"2019-08-24","specialtyPharmacyName":"CMM Pharma P","specialtyPharmacyTriageDate":"2025-08-24T14:15:22Z"}},{"serviceType":"copay","subscriptionDate":"2023-11-13","subscriptionStatus":"registrationCompleted","rxMemberId":"NEWZ83100101048"}]}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/patients/{id}/services/{brand}".format(id='id_example', brand='brand_example'),
    #    headers=headers,
    #    json=patch_patients_id_services_brand_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

