# coding: utf-8

from fastapi.testclient import TestClient

from openapi_server.models.consents_update_event import ConsentsUpdateEvent  # noqa: F401
from openapi_server.models.demographic_delete_event import DemographicDeleteEvent  # noqa: F401
from openapi_server.models.demographic_merge_event import DemographicMergeEvent  # noqa: F401
from openapi_server.models.demographic_un_merge_event import DemographicUnMergeEvent  # noqa: F401
from openapi_server.models.demographic_update_event import DemographicUpdateEvent  # noqa: F401
from openapi_server.models.enrollment_event import EnrollmentEvent  # noqa: F401
from openapi_server.models.pace_update_event import PaceUpdateEvent  # noqa: F401


def test_brand_enrollment_created_post(client: TestClient):
    """Test case for brand_enrollment_created_post

    
    """
    enrollment_event = EnrollmentEvent()

    headers = {
    }
    # uncomment below to make a request
    response = client.request(
       "POST",
       "/brand.enrollment.created",
       headers=headers,
       json=enrollment_event,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_brand_enrollment_updated_post(client: TestClient):
    """Test case for brand_enrollment_updated_post

    
    """
    enrollment_event = EnrollmentEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/brand.enrollment.updated",
    #    headers=headers,
    #    json=enrollment_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_brand_pace_updated_post(client: TestClient):
    """Test case for brand_pace_updated_post

    
    """
    pace_update_event = PaceUpdateEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/brand.pace.updated",
    #    headers=headers,
    #    json=pace_update_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_patient_consents_updated_post(client: TestClient):
    """Test case for patient_consents_updated_post

    
    """
    consents_update_event = ConsentsUpdateEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/patient.consents.updated",
    #    headers=headers,
    #    json=consents_update_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_patient_demographics_deleted_post(client: TestClient):
    """Test case for patient_demographics_deleted_post

    
    """
    demographic_delete_event = DemographicDeleteEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/patient.demographics.deleted",
    #    headers=headers,
    #    json=demographic_delete_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_patient_demographics_merged_post(client: TestClient):
    """Test case for patient_demographics_merged_post

    
    """
    demographic_merge_event = DemographicMergeEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/patient.demographics.merged",
    #    headers=headers,
    #    json=demographic_merge_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_patient_demographics_un_merged_post(client: TestClient):
    """Test case for patient_demographics_un_merged_post

    
    """
    demographic_un_merge_event = DemographicUnMergeEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/patient.demographics.unMerged",
    #    headers=headers,
    #    json=demographic_un_merge_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_patient_demographics_updated_post(client: TestClient):
    """Test case for patient_demographics_updated_post

    
    """
    demographic_update_event = DemographicUpdateEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/patient.demographics.updated",
    #    headers=headers,
    #    json=demographic_update_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_prospect_consents_updated_post(client: TestClient):
    """Test case for prospect_consents_updated_post

    
    """
    consents_update_event = ConsentsUpdateEvent()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/prospect.consents.updated",
    #    headers=headers,
    #    json=consents_update_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

