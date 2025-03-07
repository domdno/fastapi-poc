# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.enrollment_api_base import BaseEnrollmentApi
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
from openapi_server.models.error_default import ErrorDefault
from openapi_server.models.flex_enrollment import FlexEnrollment
from openapi_server.security_api import get_token_oauth2DEV

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/patients/enrollments/{brand}",
    responses={
        200: {"model": FlexEnrollment, "description": "OK.   Provides patient identifier, caregiver identifier (when applicable) as well as a URL to the patients preference center.  Any other values in the response as the same as the request.   "},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["Enrollment"],
    summary="New Patient Enrollment",
    response_model_by_alias=True,
)
async def post_patient_brand_enrollment(
    brand: Annotated[StrictStr, Field(description="Brand Name")] = Path(..., description="Brand Name"),
    flex_enrollment: Annotated[Optional[FlexEnrollment], Field(description="Patient's details and enrollment  preferences (patient demographic, consents and clinical information).")] = Body(None, description="Patient&#39;s details and enrollment  preferences (patient demographic, consents and clinical information)."),
    token_oauth2DEV: TokenModel = Security(
        get_token_oauth2DEV, scopes=[]
    ),
) -> FlexEnrollment:
    """Allows to enroll a new patient to BI. Patient will be enrolled in the specified brand by providing their contact information, consents and subscriptions to services offered by BI (through its partners).  If the patient is found to be already register in BI, their demographic information will be updated along with any non-brand specific consents (i.e., BI Corporate Communications).  """
    if not BaseEnrollmentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEnrollmentApi.subclasses[0]().post_patient_brand_enrollment(brand, flex_enrollment)


@router.post(
    "/patient-enrollment/{brand}",
    responses={
        202: {"description": "Accepted"},
        400: {"model": ErrorDefault, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        500: {"model": ErrorDefault, "description": ""},
    },
    tags=["Enrollment"],
    summary="(PSP) Websites Patient Enrollment",
    response_model_by_alias=True,
)
async def post_patient_enroll_brand_async(
    brand: Annotated[StrictStr, Field(description="Brand Name")] = Path(..., description="Brand Name"),
    flex_enrollment: Annotated[Optional[FlexEnrollment], Field(description="Patient's details and enrollment  preferences (patient demographic, consents and clinical information).  ")] = Body(None, description="Patient&#39;s details and enrollment  preferences (patient demographic, consents and clinical information).  "),
    token_oauth2DEV: TokenModel = Security(
        get_token_oauth2DEV, scopes=[]
    ),
) -> None:
    """Allows to submit a patient information for enrollment to a BI brand. The patient could be existing or new.   Depending on the accuracy of the data provided, the enrollment could be done near real time or might require additional manual processing to complete the patient enrollment. """
    if not BaseEnrollmentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEnrollmentApi.subclasses[0]().post_patient_enroll_brand_async(brand, flex_enrollment)


@router.put(
    "/patients/{id}/enrollments/{brand}",
    responses={
        200: {"model": FlexEnrollment, "description": "OK. Response values are the same as the request.   "},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["Enrollment"],
    summary="Update Patient Enrollment",
    response_model_by_alias=True,
)
async def put_patient_brand_enrollment(
    id: Annotated[StrictStr, Field(description="BI's Patient Identifier")] = Path(..., description="BI&#39;s Patient Identifier"),
    brand: Annotated[StrictStr, Field(description="Brand Name")] = Path(..., description="Brand Name"),
    flex_enrollment: Annotated[Optional[FlexEnrollment], Field(description="Patient's details and enrollment  preferences (patient demographic, consents and clinical information).")] = Body(None, description="Patient&#39;s details and enrollment  preferences (patient demographic, consents and clinical information)."),
) -> FlexEnrollment:
    """Allows to enroll an existing patient in a new BI’ HP brand or update their enrollment to a brand.  The patient will be enrolled, or their enrollment will be updated, by providing their consents and subscriptions to services offered by BI (through its partners).  BI’s patient demographic information will also be updated with the data provided and it will be distributed to any other brands where the patient could have previously enrolled.  Client applications are expected to provide the latest patient demographic available to them to any means. """
    if not BaseEnrollmentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEnrollmentApi.subclasses[0]().put_patient_brand_enrollment(id, brand, flex_enrollment)
