# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.put_patient_request import PutPatientRequest
from openapi_server.security_api import get_token_oauth2DEV, get_token_oauth2PROD, get_token_oauth2QA

class BaseDemographicApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDemographicApi.subclasses = BaseDemographicApi.subclasses + (cls,)
    async def put_patient(
        self,
        id: Annotated[StrictStr, Field(description="BI's Unique Patient Identifier")],
        put_patient_request: Annotated[Optional[PutPatientRequest], Field(description="Patient demographic data")],
    ) -> None:
        """Allows to modify current patient&#39;s demographic information without modifying any other enrollment information.  Patient&#39;s information will be modified across brands. """
        ...
