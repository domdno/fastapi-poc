# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.events_api_base import BaseEventsApi
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
from pydantic import Field
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from openapi_server.models.consents_update_event import ConsentsUpdateEvent
from openapi_server.models.error import Error
from openapi_server.models.error_default import ErrorDefault
from openapi_server.models.failed_event import FailedEvent
from openapi_server.models.pace_update_event import PaceUpdateEvent
from openapi_server.models.post_events_incidents201_response import PostEventsIncidents201Response


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/events/incidents",
    responses={
        201: {"model": PostEventsIncidents201Response, "description": "Created"},
        400: {"model": ErrorDefault, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        403: {"model": object, "description": "Forbidden"},
        500: {"model": ErrorDefault, "description": "Internal Server Error"},
    },
    tags=["Events"],
    summary="Report a post processing incident",
    response_model_by_alias=True,
)
async def post_events_incidents(
    failed_event: Optional[FailedEvent] = Body(None, description=""),
) -> PostEventsIncidents201Response:
    """Allows to report a consumer application error that requires Boehringer Ingelheim patient capability platform triage and intervention.     Use this operation to report post processing errors related to consumed events.    This this generate and incident and it will require human intervention."""
    if not BaseEventsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventsApi.subclasses[0]().post_events_incidents(failed_event)


@router.post(
    "/events/publishing/consents",
    responses={
        202: {"description": "Accepted"},
        400: {"model": ErrorDefault, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        403: {"model": object, "description": "Forbidden"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["Events"],
    summary="CPM&#39;s OTPC updates notifications",
    response_model_by_alias=True,
)
async def post_events_publishing_consents(
    consents_update_event: Annotated[Optional[ConsentsUpdateEvent], Field(description="Event to publish")] = Body(None, description="Event to publish"),
) -> None:
    """Allows to publish an consent update event to all subscribing/consumer applications.  """
    if not BaseEventsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventsApi.subclasses[0]().post_events_publishing_consents(consents_update_event)


@router.post(
    "/events/publishing/pace",
    responses={
        202: {"description": "Accepted"},
        400: {"model": ErrorDefault, "description": "Bad Request"},
        401: {"model": object, "description": "Unauthorized"},
        403: {"model": object, "description": "Forbidden"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["Events"],
    summary="PaCE updates notifications",
    response_model_by_alias=True,
)
async def post_events_publishing_pace(
    pace_update_event: Annotated[Optional[PaceUpdateEvent], Field(description="Event to publish")] = Body(None, description="Event to publish"),
) -> None:
    """Allow to publish an PaCE update events to one or more subscribing/consumer applications."""
    if not BaseEventsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventsApi.subclasses[0]().post_events_publishing_pace(pace_update_event)
