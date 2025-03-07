# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.patch_patients_id_services_brand_request import PatchPatientsIdServicesBrandRequest


class BasePaCEApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePaCEApi.subclasses = BasePaCEApi.subclasses + (cls,)
    async def patch_patients_id_services_brand(
        self,
        id: Annotated[StrictStr, Field(description="Patient Identifier (MDMID)")],
        brand: Annotated[StrictStr, Field(description="Brand where the patient has previously enrolled")],
        patch_patients_id_services_brand_request: Optional[PatchPatientsIdServicesBrandRequest],
    ) -> None:
        """Allows to provide Patient Support Program updates relevant to the patient services and health information."""
        ...
