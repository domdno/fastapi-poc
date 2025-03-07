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




from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CaseManagementService(BaseModel):
    """
    This service is provided by BI's partners HUBs. It offers continuous patient support through phone or other channels and  helps navigate any services that might be offered for the brand. 
    """ # noqa: E501
    service_type: StrictStr = Field(description="Brand specific service offered by BI that would help the patient throughout their treatment journey.", alias="serviceType")
    subscription_status: Optional[StrictStr] = Field(default=None, description="Latest status of the service Subscription", alias="subscriptionStatus")
    subscription_date: Optional[date] = Field(default=None, description="When the patient case was created in the PSP contact center (HUB).", alias="subscriptionDate")
    case_id: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="Patient's case identifier (in the external case management system) related to this patient education subscription.", alias="caseId")
    case_status: Optional[StrictStr] = Field(default=None, description="Case statusin the Patient PSP HUB data provider.", alias="caseStatus")
    patient_journey_status: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Status of the request in the (external) PSP HUB partner and lets the PaCE know if they should be reaching out to the patient.", alias="patientJourneyStatus")
    welcome_call_date: Optional[datetime] = Field(default=None, description="Patient Support Program (PSP) welcome call date (i.e. the date when the patient received the first call regarding BI Solutions Plus).", alias="welcomeCallDate")
    patient_navigator_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Reference name (first name or full name)  of the Patient Navigator who will be contacting the patient to guide the patient through clinical education program.  ", alias="patientNavigatorName")
    benefits_verification_status: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="It refers to the Benefits Verification Status of a medication. It indicates the current stage or outcome of verifying the patient’s insurance coverage and benefits for a prescribed medication.", alias="benefitsVerificationStatus")
    prior_authorization_status: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Refers to the Prior Authorization Status of a medication. It indicates the current stage or outcome of the approval process required by an insurance provider.", alias="priorAuthorizationStatus")
    prior_authorization_required: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Is the Prior Authorization (PA) submitted or not by the HCP.", alias="priorAuthorizationRequired")
    prior_authorization_expired_date: Optional[datetime] = Field(default=None, description="Expiration date of the approved Prior Authorization (PA) for the medication.", alias="priorAuthorizationExpiredDate")
    prior_authorization_identifier: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Unique Identifier of the Prior Authorization (PA).", alias="priorAuthorizationIdentifier")
    appeal_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Unique Identifier of the Appeal.", alias="appealId")
    appealed_prior_authorization_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Is the current PA is an appeal of the prior PA.", alias="appealedPriorAuthorizationId")
    __properties: ClassVar[List[str]] = ["serviceType", "subscriptionStatus", "subscriptionDate", "caseId", "caseStatus", "patientJourneyStatus", "welcomeCallDate", "patientNavigatorName", "benefitsVerificationStatus", "priorAuthorizationStatus", "priorAuthorizationRequired", "priorAuthorizationExpiredDate", "priorAuthorizationIdentifier", "appealId", "appealedPriorAuthorizationId"]

    @field_validator('service_type')
    def service_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('caseManagement',):
            raise ValueError("must be one of enum values ('caseManagement')")
        return value

    @field_validator('subscription_status')
    def subscription_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('optIn', 'optOut',):
            raise ValueError("must be one of enum values ('optIn', 'optOut')")
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
        """Create an instance of CaseManagementService from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CaseManagementService from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serviceType": obj.get("serviceType"),
            "subscriptionStatus": obj.get("subscriptionStatus"),
            "subscriptionDate": obj.get("subscriptionDate"),
            "caseId": obj.get("caseId"),
            "caseStatus": obj.get("caseStatus"),
            "patientJourneyStatus": obj.get("patientJourneyStatus"),
            "welcomeCallDate": obj.get("welcomeCallDate"),
            "patientNavigatorName": obj.get("patientNavigatorName"),
            "benefitsVerificationStatus": obj.get("benefitsVerificationStatus"),
            "priorAuthorizationStatus": obj.get("priorAuthorizationStatus"),
            "priorAuthorizationRequired": obj.get("priorAuthorizationRequired"),
            "priorAuthorizationExpiredDate": obj.get("priorAuthorizationExpiredDate"),
            "priorAuthorizationIdentifier": obj.get("priorAuthorizationIdentifier"),
            "appealId": obj.get("appealId"),
            "appealedPriorAuthorizationId": obj.get("appealedPriorAuthorizationId")
        })
        return _obj


