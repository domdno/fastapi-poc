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




from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.supply_fulfillment import SupplyFulfillment
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SupplyFulfillmentEvent(BaseModel):
    """
    Notifies that a previouly requested patient supply has changed status.
    """ # noqa: E501
    version: StrictStr = Field(description="Indicates event version type, it help to determine the schema or data format of the event.")
    created_timestamp: datetime = Field(description="Indicates when the event was initially generated and published to subscribers.", alias="createdTimestamp")
    request_id: Optional[StrictStr] = Field(default=None, description="BI's unique identifier for the event. It is the same unique identifier of the transaction that published the event. (e.g. Patient Engagement API).", alias="requestId")
    event_type: StrictStr = Field(description="Message Topic. Indicates the type of data is being sent with the event.", alias="eventType")
    data: SupplyFulfillment
    __properties: ClassVar[List[str]] = ["version", "createdTimestamp", "requestId", "eventType", "data"]

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
        """Create an instance of SupplyFulfillmentEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SupplyFulfillmentEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version": obj.get("version"),
            "createdTimestamp": obj.get("createdTimestamp"),
            "requestId": obj.get("requestId"),
            "eventType": obj.get("eventType"),
            "data": SupplyFulfillment.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        return _obj


