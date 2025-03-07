# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.patch_patient_consents_brand200_response import PatchPatientConsentsBrand200Response
from openapi_server.models.patch_patient_consents_brand_request import PatchPatientConsentsBrandRequest
from openapi_server.security_api import get_token_oauth2DEV, get_token_oauth2PROD, get_token_oauth2QA

class BaseConsentApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseConsentApi.subclasses = BaseConsentApi.subclasses + (cls,)
    async def patch_patient_consents_brand(
        self,
        id: Annotated[StrictStr, Field(description="BI's Unique Patient Identifier")],
        patch_patient_consents_brand_request: Annotated[Optional[PatchPatientConsentsBrandRequest], Field(description="Patient updated consents and preferences")],
    ) -> PatchPatientConsentsBrand200Response:
        """Allows to update patient&#39;s consents and preferences for a brand. It will also allow to opt-out a patient from all BI Corporate communications (which will unsubscribe the patient from all BI&#39;s brands and services)."""
        ...
