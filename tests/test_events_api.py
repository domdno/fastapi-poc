# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field  # noqa: F401
from typing import Any, Dict, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.consents_update_event import ConsentsUpdateEvent  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.error_default import ErrorDefault  # noqa: F401
from openapi_server.models.failed_event import FailedEvent  # noqa: F401
from openapi_server.models.pace_update_event import PaceUpdateEvent  # noqa: F401
from openapi_server.models.post_events_incidents201_response import PostEventsIncidents201Response  # noqa: F401


def test_post_events_incidents(client: TestClient):
    """Test case for post_events_incidents

    Report a post processing incident
    """
    failed_event = {"error_timestamp":"2000-01-23T04:56:07.000+00:00","event_consumer":"eventConsumer","error_transaction_reference":"errorTransactionReference","error_message":"errorMessage","error_id":"errorId","event":{"data":{"consents_and_preferences":[{"preferences":[{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]}],"name":"Patient Support Program Communications","status":"optOut"},{"preferences":[{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]}],"name":"Patient Support Program Communications","status":"optOut"}],"insurance_plans":[{"specialty_pharmacy_npi":"specialtyPharmacyNPI","plan_type":"pharmacy","policyholder_birth_date":"2000-01-23","provider_phone_number":"providerPhoneNumber","plan_name":"planName","policyholder_name":"policyholderName","rx_pcn":"rxPcn","specialty_pharmacy_preferred":"specialtyPharmacyPreferred","medication_tier":"medicationTier","group_number":"groupNumber","individual_deductible":"individualDeductible","insurance_hierarchy":"insuranceHierarchy","provider":"provider","family_deductible":"familyDeductible","provider_payer_type":"providerPayerType","coinsurance_percentage":"coinsurancePercentage","max_out_of_pocket_total":"maxOutOfPocketTotal","specialty_pharmacy_required":"specialtyPharmacyRequired","rx_bin":"rxBin","member_id":"memberId"},{"specialty_pharmacy_npi":"specialtyPharmacyNPI","plan_type":"pharmacy","policyholder_birth_date":"2000-01-23","provider_phone_number":"providerPhoneNumber","plan_name":"planName","policyholder_name":"policyholderName","rx_pcn":"rxPcn","specialty_pharmacy_preferred":"specialtyPharmacyPreferred","medication_tier":"medicationTier","group_number":"groupNumber","individual_deductible":"individualDeductible","insurance_hierarchy":"insuranceHierarchy","provider":"provider","family_deductible":"familyDeductible","provider_payer_type":"providerPayerType","coinsurance_percentage":"coinsurancePercentage","max_out_of_pocket_total":"maxOutOfPocketTotal","specialty_pharmacy_required":"specialtyPharmacyRequired","rx_bin":"rxBin","member_id":"memberId"}],"marketing_campaign_source_code":"marketingCampaignSourceCode","enrollment_date":"2000-01-23","insurance_types":["commertial","commertial","commertial","commertial","commertial"],"data_provider_id":"dataProviderId","preferences_link_token":"preferencesLinkToken","service_subscriptions":[{"service_type":"demoDeviceAutoInjection","subscription_date":"2000-01-23","subscription_status":"optIn"},{"service_type":"demoDeviceAutoInjection","subscription_date":"2000-01-23","subscription_status":"optIn"}],"primary_hcp":{"first_name":"firstName","last_name":"lastName","practice_name":"practiceName","medical_license_number:":"medicalLicenseNumber:","phones":[{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"}],"medical_speciality":"medicalSpeciality","national_provider_identifier":"nationalProviderIdentifier"},"applicant_type":"patient","patient":{"last_name":"lastName","preferred_language_code":"preferredLanguageCode","gender":"male","city":"Lexington","alternate_contact":{"email_address":"emailAddress","phone_number":"phoneNumber","relationship_to_patient":"relationshipToPatient","full_name":"fullName"},"postal_code":"02420-5303","name_suffix_code":"II","enriched_indicator":"enrichedIndicator","state_or_province_code":"MA","birth_date":"2000-01-23","first_name":"firstName","communications":[{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"}],"country_code":"US","address_line1":"874 Massachusetts Avenue","middle_name":"Junior","address_line2":"addressLine2","id":"MDM000001T3BKL","name_prefix_code":"MR"},"prescribing_hcp":{"last_name":"lastName","city":"Lexington","medical_license_number:":"medicalLicenseNumber:","postal_code":"02420-5303","phones":[{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"}],"enriched_indicator":"enrichedIndicator","state_or_province_code":"MA","first_name":"firstName","practice_name":"practiceName","country_code":"US","office_contact":{"email_address":"emailAddress","direct_phone_number":"directPhoneNumber","full_name":"fullName"},"address_line1":"874 Massachusetts Avenue","address_line2":"addressLine2","medical_speciality":"medicalSpeciality","national_provider_identifier":"nationalProviderIdentifier"},"data_provider_transaction_id":"dataProviderTransactionId","data_provider_patient_id":"dataProviderPatientId","clinical_details":{"prior_treatments":["priorTreatments","priorTreatments","priorTreatments","priorTreatments","priorTreatments"],"drug_allergies":["drugAllergies","drugAllergies","drugAllergies","drugAllergies","drugAllergies"],"brand_adherence":"brandAdherence","prescription":{"quantity":6027.456183070403,"drug_group":"drugGroup","add_ons":"addOns","drug_form":"drugForm","medication_tier":"medicationTier","refills":1.4658129805029452,"specialty_pharmacy_triage_date":"2000-01-23T04:56:07.000+00:00","drug_strength":"drugStrength","signature_date":"2000-01-23","specialty_pharmacy_name":"specialtyPharmacyName","drug_name":"drugName","dispense_as_written":"dispenseAsWritten","shipped_date":"2000-01-23","status":"status","ship_to":"patient"},"diagnosis_date":"2000-01-23","support_persons_number":8.008281904610115,"icd_code":"icdCode","concomitant_medications":"concomitantMedications","indication":"indication","last_dose_date":"2000-01-23","therapy_start_date":"2000-01-23"}},"request_id":"1d93f893-d28e-4fff-afc3-0ae8ad403c59","created_timestamp":"2000-01-23T04:56:07.000+00:00","event_type":"zongertinib.enrollment.created","version":"1.0"}}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/events/incidents",
    #    headers=headers,
    #    json=failed_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_post_events_publishing_consents(client: TestClient):
    """Test case for post_events_publishing_consents

    CPM's OTPC updates notifications
    """
    consents_update_event = {"data":{"consents_and_preferences":[{"preferences":[{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]}],"name":"Patient Support Program Communications","status":"optOut"},{"preferences":[{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]}],"name":"Patient Support Program Communications","status":"optOut"}],"individual_id":"individualId","data_provider_id":"dataProviderId"},"request_id":"1d93f893-d28e-4fff-afc3-0ae8ad403c59","created_timestamp":"2000-01-23T04:56:07.000+00:00","event_type":"patient.consents.updated","version":"1.0"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/events/publishing/consents",
    #    headers=headers,
    #    json=consents_update_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_post_events_publishing_pace(client: TestClient):
    """Test case for post_events_publishing_pace

    PaCE updates notifications
    """
    pace_update_event = {"data":{"service_subscriptions":[{"service_type":"demoDeviceAutoInjection","subscription_date":"2000-01-23","subscription_status":"optIn"},{"service_type":"demoDeviceAutoInjection","subscription_date":"2000-01-23","subscription_status":"optIn"},{"service_type":"demoDeviceAutoInjection","subscription_date":"2000-01-23","subscription_status":"optIn"},{"service_type":"demoDeviceAutoInjection","subscription_date":"2000-01-23","subscription_status":"optIn"},{"service_type":"demoDeviceAutoInjection","subscription_date":"2000-01-23","subscription_status":"optIn"}],"patient_id":"patientId","insurance_plans":[{"specialty_pharmacy_npi":"specialtyPharmacyNPI","plan_type":"pharmacy","policyholder_birth_date":"2000-01-23","provider_phone_number":"providerPhoneNumber","plan_name":"planName","policyholder_name":"policyholderName","rx_pcn":"rxPcn","specialty_pharmacy_preferred":"specialtyPharmacyPreferred","medication_tier":"medicationTier","group_number":"groupNumber","individual_deductible":"individualDeductible","insurance_hierarchy":"insuranceHierarchy","provider":"provider","family_deductible":"familyDeductible","provider_payer_type":"providerPayerType","coinsurance_percentage":"coinsurancePercentage","max_out_of_pocket_total":"maxOutOfPocketTotal","specialty_pharmacy_required":"specialtyPharmacyRequired","rx_bin":"rxBin","member_id":"memberId"},{"specialty_pharmacy_npi":"specialtyPharmacyNPI","plan_type":"pharmacy","policyholder_birth_date":"2000-01-23","provider_phone_number":"providerPhoneNumber","plan_name":"planName","policyholder_name":"policyholderName","rx_pcn":"rxPcn","specialty_pharmacy_preferred":"specialtyPharmacyPreferred","medication_tier":"medicationTier","group_number":"groupNumber","individual_deductible":"individualDeductible","insurance_hierarchy":"insuranceHierarchy","provider":"provider","family_deductible":"familyDeductible","provider_payer_type":"providerPayerType","coinsurance_percentage":"coinsurancePercentage","max_out_of_pocket_total":"maxOutOfPocketTotal","specialty_pharmacy_required":"specialtyPharmacyRequired","rx_bin":"rxBin","member_id":"memberId"},{"specialty_pharmacy_npi":"specialtyPharmacyNPI","plan_type":"pharmacy","policyholder_birth_date":"2000-01-23","provider_phone_number":"providerPhoneNumber","plan_name":"planName","policyholder_name":"policyholderName","rx_pcn":"rxPcn","specialty_pharmacy_preferred":"specialtyPharmacyPreferred","medication_tier":"medicationTier","group_number":"groupNumber","individual_deductible":"individualDeductible","insurance_hierarchy":"insuranceHierarchy","provider":"provider","family_deductible":"familyDeductible","provider_payer_type":"providerPayerType","coinsurance_percentage":"coinsurancePercentage","max_out_of_pocket_total":"maxOutOfPocketTotal","specialty_pharmacy_required":"specialtyPharmacyRequired","rx_bin":"rxBin","member_id":"memberId"},{"specialty_pharmacy_npi":"specialtyPharmacyNPI","plan_type":"pharmacy","policyholder_birth_date":"2000-01-23","provider_phone_number":"providerPhoneNumber","plan_name":"planName","policyholder_name":"policyholderName","rx_pcn":"rxPcn","specialty_pharmacy_preferred":"specialtyPharmacyPreferred","medication_tier":"medicationTier","group_number":"groupNumber","individual_deductible":"individualDeductible","insurance_hierarchy":"insuranceHierarchy","provider":"provider","family_deductible":"familyDeductible","provider_payer_type":"providerPayerType","coinsurance_percentage":"coinsurancePercentage","max_out_of_pocket_total":"maxOutOfPocketTotal","specialty_pharmacy_required":"specialtyPharmacyRequired","rx_bin":"rxBin","member_id":"memberId"},{"specialty_pharmacy_npi":"specialtyPharmacyNPI","plan_type":"pharmacy","policyholder_birth_date":"2000-01-23","provider_phone_number":"providerPhoneNumber","plan_name":"planName","policyholder_name":"policyholderName","rx_pcn":"rxPcn","specialty_pharmacy_preferred":"specialtyPharmacyPreferred","medication_tier":"medicationTier","group_number":"groupNumber","individual_deductible":"individualDeductible","insurance_hierarchy":"insuranceHierarchy","provider":"provider","family_deductible":"familyDeductible","provider_payer_type":"providerPayerType","coinsurance_percentage":"coinsurancePercentage","max_out_of_pocket_total":"maxOutOfPocketTotal","specialty_pharmacy_required":"specialtyPharmacyRequired","rx_bin":"rxBin","member_id":"memberId"}],"data_provider_patient_id":"dataProviderPatientId","data_provider_id":"dataProviderId"},"request_id":"1d93f893-d28e-4fff-afc3-0ae8ad403c59","created_timestamp":"2000-01-23T04:56:07.000+00:00","event_type":"zongertinib.pace.updated","version":"1.0"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/events/publishing/pace",
    #    headers=headers,
    #    json=pace_update_event,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

