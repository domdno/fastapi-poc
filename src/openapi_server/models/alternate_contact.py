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




from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AlternateContact(BaseModel):
    """
    Contact information of a person that occacionally assists the patient in their health journey (without having any legal rights or obligations). This information is NOT intended to capture the patient owns phone numbers or their caregiver or guardian phone numbers. 
    """ # noqa: E501
    full_name: Annotated[str, Field(min_length=1, strict=True, max_length=100)] = Field(description="Indicates the first and last name(s) of the person that will be answering the phone call.", alias="fullName")
    relationship_to_patient: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="Indicates how this person is related to the patient.", alias="relationshipToPatient")
    phone_number: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=15)]] = Field(default=None, description="Alternate contact phone number.", alias="phoneNumber")
    email_address: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="Alternate contact email address", alias="emailAddress")
    __properties: ClassVar[List[str]] = ["fullName", "relationshipToPatient", "phoneNumber", "emailAddress"]

    @field_validator('phone_number')
    def phone_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
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
        """Create an instance of AlternateContact from a JSON string"""
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
        """Create an instance of AlternateContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fullName": obj.get("fullName"),
            "relationshipToPatient": obj.get("relationshipToPatient"),
            "phoneNumber": obj.get("phoneNumber"),
            "emailAddress": obj.get("emailAddress")
        })
        return _obj


