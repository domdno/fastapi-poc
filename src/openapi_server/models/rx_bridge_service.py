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

class RxBridgeService(BaseModel):
    """
    Bridge Program may provide a limited supply of [BRAND] to eligible patients who are experiencing a coverage delay or denial.
    """ # noqa: E501
    service_type: StrictStr = Field(description="Brand specific service offered by BI that would help the patient throughout their treatment journey.", alias="serviceType")
    subscription_status: Optional[StrictStr] = Field(default=None, description="Latest status of the service Subscription", alias="subscriptionStatus")
    subscription_date: Optional[date] = Field(default=None, description="When the patient agreed to receib Brige service, either by signing a form or by communicating it ververbaly to the PSP HUB.", alias="subscriptionDate")
    prescription: Dict[str, Any]
    bridge_status: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The name of the pharmacy responsible for shipping the medication to the patient.", alias="bridgeStatus")
    triage_date: Optional[datetime] = Field(default=None, description="Indicates the date on which the patient's medication shipment request or issue was reviewed and prioritized.", alias="triageDate")
    intake_date: Optional[datetime] = Field(default=None, description="Date on which the bridge was requested for the patient after eligibility verification.  The date in which the PSP Hub triages the Rx to the program pharmacy.", alias="intakeDate")
    __properties: ClassVar[List[str]] = ["serviceType", "subscriptionStatus", "subscriptionDate", "prescription", "bridgeStatus", "triageDate", "intakeDate"]

    @field_validator('service_type')
    def service_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('rxBridge',):
            raise ValueError("must be one of enum values ('rxBridge')")
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
        """Create an instance of RxBridgeService from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of prescription
        if self.prescription:
            _dict['prescription'] = self.prescription.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RxBridgeService from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serviceType": obj.get("serviceType"),
            "subscriptionStatus": obj.get("subscriptionStatus"),
            "subscriptionDate": obj.get("subscriptionDate"),
            "prescription": Prescription.from_dict(obj.get("prescription")) if obj.get("prescription") is not None else None,
            "bridgeStatus": obj.get("bridgeStatus"),
            "triageDate": obj.get("triageDate"),
            "intakeDate": obj.get("intakeDate")
        })
        return _obj


