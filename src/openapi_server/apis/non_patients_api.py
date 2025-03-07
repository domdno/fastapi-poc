# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.non_patients_api_base import BaseNonPatientsApi
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
from typing import Any, Dict, Optional
from typing_extensions import Annotated


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/prospects/{brand}",
    responses={
        202: {"description": "Accepted"},
        400: {"model": ErrorDefault, "description": "Bad Request"},
        401: {"description": "Unauthorized"},
        500: {"model": ErrorDefault, "description": "Internal Server Error"},
    },
    tags=["Non-Patients"],
    summary="New Marketing signup",
    response_model_by_alias=True,
)
async def post_prospects(
    brand: Annotated[StrictStr, Field(description="Brand Name")] = Path(..., description="Brand Name"),
    prospect_registration: Optional[Dict[str, Any]] = Body(None, description=""),
) -> None:
    """Allows patients or general public to sign up to receive more (marketing) information about a Boehringer Ingelheim brand. """
    if not BaseNonPatientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNonPatientsApi.subclasses[0]().post_prospects(brand, prospect_registration)
