# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401 # type: ignore
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
from openapi_server.models.consents_update_event import ConsentsUpdateEvent
from openapi_server.models.demographic_delete_event import DemographicDeleteEvent
from openapi_server.models.demographic_merge_event import DemographicMergeEvent
from openapi_server.models.demographic_un_merge_event import DemographicUnMergeEvent
from openapi_server.models.demographic_update_event import DemographicUpdateEvent
from openapi_server.models.enrollment_event import EnrollmentEvent
from openapi_server.models.pace_update_event import PaceUpdateEvent


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/brand.enrollment.created",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def brand_enrollment_created_post(
    enrollment_event  = Body(None, description="Notifies when a new patient registers for first time into a brand or re-enrolls to a brand via the brand website."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().brand_enrollment_created_post(enrollment_event)


@router.post(
    "/brand.enrollment.updated",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def brand_enrollment_updated_post(
    enrollment_event  = Body(None, description="Notifies when a patient needs to update their brand enrollment information (e.g., demographic, consents, insurance, start/stop services, etc.)"),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().brand_enrollment_updated_post(enrollment_event)


@router.post(
    "/brand.pace.updated",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def brand_pace_updated_post(
    pace_update_event  = Body(None, description="Notifies the patient interaction results with a Clinical Educator (for participating patients)."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().brand_pace_updated_post(pace_update_event)


@router.post(
    "/patient.consents.updated",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def patient_consents_updated_post(
    consents_update_event  = Body(None, description="Notifies when a patient has updated their consents to a brand program."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().patient_consents_updated_post(consents_update_event)


@router.post(
    "/patient.demographics.deleted",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def patient_demographics_deleted_post(
    demographic_delete_event  = Body(None, description="Notifies when a patient has requested their data to be forgotten."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().patient_demographics_deleted_post(demographic_delete_event)


@router.post(
    "/patient.demographics.merged",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def patient_demographics_merged_post(
    demographic_merge_event  = Body(None, description="Notifies when a manual data stewardship process finds two records match the same patient."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().patient_demographics_merged_post(demographic_merge_event)


@router.post(
    "/patient.demographics.unMerged",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def patient_demographics_un_merged_post(
    demographic_un_merge_event  = Body(None, description="Notfies when a manual data stewardship process found one record represents two different patients."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().patient_demographics_un_merged_post(demographic_un_merge_event)


@router.post(
    "/patient.demographics.updated",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def patient_demographics_updated_post(
    demographic_update_event  = Body(None, description="Notifies when a patient (or their legal caregiver or guardian) has updated their demographic information (across all Boehringer Ingelheim brands)."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().patient_demographics_updated_post(demographic_update_event)


@router.post(
    "/prospect.consents.updated",
    responses={
        200: {"description": "Return a 200 status to indicate that the data was received successfully"},
        202: {"description": "Return a 202 status to indicate that the data was received successfully"},
        400: {"description": "Return a 400 status to indicate the event format or values are invalid"},
        401: {"description": "Return a 401 status to indicate that credentials provided are invalid"},
        403: {"description": "Return a 403 status to indicate that credentials provided are unauthorized"},
        429: {"description": "Return a 429 status to indicate that too many request and the system cannot handle them at the moment and need to try again later"},
        500: {"description": "Return a 500 status to indicate a temporarily system error and need to try again later"},
        502: {"description": "Return a 502 status to indicate that the the mesasge could not be delived and need to try again later"},
        503: {"description": "Return a 503 status to indicate that the system is temporarily unavailable and need to try again later"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def prospect_consents_updated_post(
    consents_update_event  = Body(None, description="Notifies when a non-patient has updated their consents to a brand signup."),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().prospect_consents_updated_post(consents_update_event)
