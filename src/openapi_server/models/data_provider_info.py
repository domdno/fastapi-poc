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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DataProviderInfo(BaseModel):
    """
    Describes the entity or BI Partner that provides the data for processing. 
    """ # noqa: E501
    data_provider_id: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="BI assigned partner unique identifier for a particular partner channel used to gather the Patient's information. For example if the same parter has web and phone changel, then there will be two unique identifier for the same partner one for web and another for phone. ", alias="dataProviderId")
    data_provider_patient_id: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="External BI partner/vendor patient Identifier. If the client application does not keep a patient Id (i.e. brand websites) then provide the same dataProviderTransactionId. ", alias="dataProviderPatientId")
    data_provider_transaction_id: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="External BI partner transaction Id (for Incident management, allows E2E tracing of this request)", alias="dataProviderTransactionId")
    __properties: ClassVar[List[str]] = ["dataProviderId", "dataProviderPatientId", "dataProviderTransactionId"]

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
        """Create an instance of DataProviderInfo from a JSON string"""
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
        """Create an instance of DataProviderInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataProviderId": obj.get("dataProviderId"),
            "dataProviderPatientId": obj.get("dataProviderPatientId"),
            "dataProviderTransactionId": obj.get("dataProviderTransactionId")
        })
        return _obj


