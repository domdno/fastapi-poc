# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.pa_ce_api_base import BasePaCEApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.patch_patients_id_services_brand_request import PatchPatientsIdServicesBrandRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.patch(
    "/patients/{id}/services/{brand}",
    responses={
        202: {"description": "Accepted"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["PaCE"],
    summary="Update Patient Services",
    response_model_by_alias=True,
)
async def patch_patients_id_services_brand(
    id: Annotated[StrictStr, Field(description="Patient Identifier (MDMID)")] = Path(..., description="Patient Identifier (MDMID)"),
    brand: Annotated[StrictStr, Field(description="Brand where the patient has previously enrolled")] = Path(..., description="Brand where the patient has previously enrolled"),
    patch_patients_id_services_brand_request: Optional[PatchPatientsIdServicesBrandRequest] = Body(None, description=""),
) -> None:
    """Allows to provide Patient Support Program updates relevant to the patient services and health information."""
    if not BasePaCEApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePaCEApi.subclasses[0]().patch_patients_id_services_brand(id, brand, patch_patients_id_services_brand_request)
