# coding: utf-8

"""
    Patient Engagement Enterprise API

    Patient Engagement Enterprise API allows multiple communication channels (e.g. websites,  HUbs, etc.) to enrroll and/or manage patient's support porgrams and services offered by Boehringer Ingelheim brands.  

    The version of the OpenAPI document: 0.7.1
    Contact: zzITEDPPatientEngagementIntegration@boehringer-ingelheim.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.clinical_details import ClinicalDetails
from openapi_server.models.consent import Consent
from openapi_server.models.health_care_practitioner import HealthCarePractitioner
from openapi_server.models.insurance_plan import InsurancePlan
from openapi_server.models.patient import Patient
from openapi_server.models.prescribing_hcp import PrescribingHCP
from openapi_server.models.service_subscription import ServiceSubscription
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FlexEnrollment(BaseModel):
    """
    Patient's required and optional data that could or must be captured to enroll patients in one or more of Boehringer Ingelheim's patient programs such as a brand's Patient Support Program (PSP)
    """ # noqa: E501
    data_provider_id: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="BI assigned partner unique identifier for a particular partner channel used to gather the Patient's information. For example if the same parter has web and phone changel, then there will be two unique identifier for the same partner one for web and another for phone. ", alias="dataProviderId")
    data_provider_patient_id: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="External BI partner/vendor patient Identifier. If the client application does not keep a patient Id (i.e. brand websites) then provide the same dataProviderTransactionId. ", alias="dataProviderPatientId")
    data_provider_transaction_id: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="External BI partner transaction Id (for Incident management, allows E2E tracing of this request)", alias="dataProviderTransactionId")
    patient: Patient
    consents_and_preferences: Annotated[List[Consent], Field(min_length=1)] = Field(description="List of consents, attestations and opt-ins and opt-outs the patient has provided to BI and partners", alias="consentsAndPreferences")
    preferences_link_token: Optional[StrictStr] = Field(default=None, description="Personalized individual's token to a BI's Preference Center where a patient can manage their consents and preferences.", alias="preferencesLinkToken")
    applicant_type: Optional[StrictStr] = Field(default=None, description="Individual who is providing the information and consents to enroll the patient (i.e., patient or caregiver)", alias="applicantType")
    enrollment_date: Optional[date] = Field(default=None, description="Patient Support Program (PSP) enrollment date (i.e.  the date when the patient enrolled to BI Solutions Plus). ", alias="enrollmentDate")
    clinical_details: Optional[ClinicalDetails] = Field(default=None, alias="clinicalDetails")
    prescribing_hcp: Optional[PrescribingHCP] = Field(default=None, alias="prescribingHCP")
    primary_hcp: Optional[HealthCarePractitioner] = Field(default=None, alias="primaryHCP")
    insurance_types: Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True, max_length=255)]], Field(min_length=1, max_length=10)]] = Field(default=None, description="Indicates one or more medical insurance plans are available and the plans types.  For example:  Commercial  Health Exchange  Managed Medicaid  Medicare  State Medicaid  TRICARE  VA  Other Government  ", alias="insuranceTypes")
    insurance_plans: Optional[List[InsurancePlan]] = Field(default=None, description="Patient's list of pharmacy insurance plans.", alias="insurancePlans")
    service_subscriptions: Optional[Annotated[List[ServiceSubscription], Field(min_length=1)]] = Field(default=None, description="List of services selected by the applicant,  and offered by BI for the brand and region, that will help the patient throughout their treatment journey", alias="serviceSubscriptions")
    marketing_campaign_source_code: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Represents the (detailed) source of the data.  A source code is used for tracking leads in the marketing system.  One source code each enrollment channel will be setup for every brand for program launch.       ", alias="marketingCampaignSourceCode")
    __properties: ClassVar[List[str]] = ["dataProviderId", "dataProviderPatientId", "dataProviderTransactionId", "patient", "consentsAndPreferences", "preferencesLinkToken", "applicantType", "enrollmentDate", "clinicalDetails", "prescribingHCP", "primaryHCP", "insuranceTypes", "insurancePlans", "serviceSubscriptions", "marketingCampaignSourceCode"]

    @field_validator('applicant_type')
    def applicant_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('patient', 'legalCaregiverOrGuardian',):
            raise ValueError("must be one of enum values ('patient', 'legalCaregiverOrGuardian')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FlexEnrollment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "preferences_link_token",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of patient
        if self.patient:
            _dict['patient'] = self.patient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in consents_and_preferences (list)
        _items = []
        if self.consents_and_preferences:
            for _item in self.consents_and_preferences:
                if _item:
                    _items.append(_item.to_dict())
            _dict['consentsAndPreferences'] = _items
        # override the default output from pydantic by calling `to_dict()` of clinical_details
        if self.clinical_details:
            _dict['clinicalDetails'] = self.clinical_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prescribing_hcp
        if self.prescribing_hcp:
            _dict['prescribingHCP'] = self.prescribing_hcp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_hcp
        if self.primary_hcp:
            _dict['primaryHCP'] = self.primary_hcp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in insurance_plans (list)
        _items = []
        if self.insurance_plans:
            for _item in self.insurance_plans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['insurancePlans'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_subscriptions (list)
        _items = []
        if self.service_subscriptions:
            for _item in self.service_subscriptions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceSubscriptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FlexEnrollment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataProviderId": obj.get("dataProviderId"),
            "dataProviderPatientId": obj.get("dataProviderPatientId"),
            "dataProviderTransactionId": obj.get("dataProviderTransactionId"),
            "patient": Patient.from_dict(obj.get("patient")) if obj.get("patient") is not None else None,
            "consentsAndPreferences": [Consent.from_dict(_item) for _item in obj.get("consentsAndPreferences")] if obj.get("consentsAndPreferences") is not None else None,
            "preferencesLinkToken": obj.get("preferencesLinkToken"),
            "applicantType": obj.get("applicantType"),
            "enrollmentDate": obj.get("enrollmentDate"),
            "clinicalDetails": ClinicalDetails.from_dict(obj.get("clinicalDetails")) if obj.get("clinicalDetails") is not None else None,
            "prescribingHCP": PrescribingHCP.from_dict(obj.get("prescribingHCP")) if obj.get("prescribingHCP") is not None else None,
            "primaryHCP": HealthCarePractitioner.from_dict(obj.get("primaryHCP")) if obj.get("primaryHCP") is not None else None,
            "insuranceTypes": obj.get("insuranceTypes"),
            "insurancePlans": [InsurancePlan.from_dict(_item) for _item in obj.get("insurancePlans")] if obj.get("insurancePlans") is not None else None,
            "serviceSubscriptions": [ServiceSubscription.from_dict(_item) for _item in obj.get("serviceSubscriptions")] if obj.get("serviceSubscriptions") is not None else None,
            "marketingCampaignSourceCode": obj.get("marketingCampaignSourceCode")
        })
        return _obj


