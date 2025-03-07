# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.demographic_api_base import BaseDemographicApi
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
from openapi_server.models.error import Error
from openapi_server.models.put_patient_request import PutPatientRequest
from openapi_server.security_api import get_token_oauth2DEV, get_token_oauth2PROD, get_token_oauth2QA

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.put(
    "/patients/{id}",
    responses={
        204: {"description": "No Content"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["Demographic"],
    summary="Update Patient&#39;s demographic",
    response_model_by_alias=True,
)
async def put_patient(
    id: Annotated[StrictStr, Field(description="BI's Unique Patient Identifier")] = Path(..., description="BI&#39;s Unique Patient Identifier"),
    put_patient_request: Annotated[Optional[PutPatientRequest], Field(description="Patient demographic data")] = Body(None, description="Patient demographic data"),
    token_oauth2DEV: TokenModel = Security(
        get_token_oauth2DEV, scopes=[]
    ),
    token_oauth2PROD: TokenModel = Security(
        get_token_oauth2PROD, scopes=[]
    ),
    token_oauth2QA: TokenModel = Security(
        get_token_oauth2QA, scopes=[]
    ),
) -> None:
    """Allows to modify current patient&#39;s demographic information without modifying any other enrollment information.  Patient&#39;s information will be modified across brands. """
    if not BaseDemographicApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDemographicApi.subclasses[0]().put_patient(id, put_patient_request)
