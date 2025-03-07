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




from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.phone import Phone
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HealthCarePractitionerAnyOf(BaseModel):
    """
    HealthCarePractitionerAnyOf
    """ # noqa: E501
    practice_name: Annotated[str, Field(min_length=0, strict=True, max_length=255)] = Field(description="Name of the business where the Health Care Practitioner operates", alias="practiceName")
    medical_speciality: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="Doctor's area of medical expertise in  which he or she has been trained and can provide patient care. ", alias="medicalSpeciality")
    national_provider_identifier: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=30)]] = Field(default=None, description="In USA, also known as NPI, a unique 10-digit identification number issued to health care providers in the United States by the Centers for Medicare and Medicaid Service.", alias="nationalProviderIdentifier")
    medical_license_number_: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=30)]] = Field(default=None, description="Unique number granted and provided by the state where the HPC if practicing medicine.", alias="medicalLicenseNumber:")
    first_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="Individual's first/given name", alias="firstName")
    last_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="Individual's legal Last/Family Name", alias="lastName")
    phones: Optional[Annotated[List[Phone], Field(min_length=1, max_length=10)]] = Field(default=None, description="List of phone numbers to conctact the patient")
    __properties: ClassVar[List[str]] = ["practiceName", "medicalSpeciality", "nationalProviderIdentifier", "medicalLicenseNumber:", "firstName", "lastName", "phones"]

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
        """Create an instance of HealthCarePractitionerAnyOf from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in phones (list)
        _items = []
        if self.phones:
            for _item in self.phones:
                if _item:
                    _items.append(_item.to_dict())
            _dict['phones'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HealthCarePractitionerAnyOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "practiceName": obj.get("practiceName"),
            "medicalSpeciality": obj.get("medicalSpeciality"),
            "nationalProviderIdentifier": obj.get("nationalProviderIdentifier"),
            "medicalLicenseNumber:": obj.get("medicalLicenseNumber:"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "phones": [Phone.from_dict(_item) for _item in obj.get("phones")] if obj.get("phones") is not None else None
        })
        return _obj


