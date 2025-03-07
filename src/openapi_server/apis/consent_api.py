# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.consent_api_base import BaseConsentApi
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
from openapi_server.models.patch_patient_consents_brand200_response import PatchPatientConsentsBrand200Response
from openapi_server.models.patch_patient_consents_brand_request import PatchPatientConsentsBrandRequest
from openapi_server.security_api import get_token_oauth2DEV, get_token_oauth2PROD, get_token_oauth2QA

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.patch(
    "/patients/{id}/consents",
    responses={
        200: {"model": PatchPatientConsentsBrand200Response, "description": "OK"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["Consent"],
    summary="Update Consents and Preferences",
    response_model_by_alias=True,
)
async def patch_patient_consents_brand(
    id: Annotated[StrictStr, Field(description="BI's Unique Patient Identifier")] = Path(..., description="BI&#39;s Unique Patient Identifier"),
    patch_patient_consents_brand_request: Annotated[Optional[PatchPatientConsentsBrandRequest], Field(description="Patient updated consents and preferences")] = Body(None, description="Patient updated consents and preferences"),
    token_oauth2DEV: TokenModel = Security(
        get_token_oauth2DEV, scopes=[]
    ),
    token_oauth2PROD: TokenModel = Security(
        get_token_oauth2PROD, scopes=[]
    ),
    token_oauth2QA: TokenModel = Security(
        get_token_oauth2QA, scopes=[]
    ),
) -> PatchPatientConsentsBrand200Response:
    """Allows to update patient&#39;s consents and preferences for a brand. It will also allow to opt-out a patient from all BI Corporate communications (which will unsubscribe the patient from all BI&#39;s brands and services)."""
    if not BaseConsentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseConsentApi.subclasses[0]().patch_patient_consents_brand(id, patch_patient_consents_brand_request)
