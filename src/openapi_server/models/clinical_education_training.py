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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClinicalEducationTraining(BaseModel):
    """
    Training Data captured during patient education classes conducted by Clinical Educators
    """ # noqa: E501
    interaction_number: Optional[StrictStr] = Field(default=None, description="TBD", alias="interactionNumber")
    type: Optional[StrictStr] = Field(default=None, description="Format of training delivery such as: oneToOne, group")
    format: Optional[StrictStr] = Field(default=None, description="faceToface, remote")
    channel: Optional[StrictStr] = Field(default=None, description="faceTime, teleConference, webcast")
    topic: Optional[StrictStr] = Field(default=None, description="Possible values:  - IPF/OFEV  - SSC-ILD/Ofev  - Chronic Fibrosing-ILD/OFEV")
    status: Optional[StrictStr] = Field(default=None, description="Possible values:  - Saved  - Completed    scheduled  completed  reScheduled ?  noShow ?")
    training_date: Optional[date] = Field(default=None, alias="trainingDate")
    completion_date: Optional[date] = Field(default=None, alias="completionDate")
    __properties: ClassVar[List[str]] = ["interactionNumber", "type", "format", "channel", "topic", "status", "trainingDate", "completionDate"]

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
        """Create an instance of ClinicalEducationTraining from a JSON string"""
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
        """Create an instance of ClinicalEducationTraining from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interactionNumber": obj.get("interactionNumber"),
            "type": obj.get("type"),
            "format": obj.get("format"),
            "channel": obj.get("channel"),
            "topic": obj.get("topic"),
            "status": obj.get("status"),
            "trainingDate": obj.get("trainingDate"),
            "completionDate": obj.get("completionDate")
        })
        return _obj


