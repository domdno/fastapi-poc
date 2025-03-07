# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from openapi_server.models.consents_update_event import ConsentsUpdateEvent
from openapi_server.models.error import Error
from openapi_server.models.error_default import ErrorDefault
from openapi_server.models.failed_event import FailedEvent
from openapi_server.models.pace_update_event import PaceUpdateEvent
from openapi_server.models.post_events_incidents201_response import PostEventsIncidents201Response


class BaseEventsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEventsApi.subclasses = BaseEventsApi.subclasses + (cls,)
    async def post_events_incidents(
        self,
        failed_event: Optional[FailedEvent],
    ) -> PostEventsIncidents201Response:
        """Allows to report a consumer application error that requires Boehringer Ingelheim patient capability platform triage and intervention.     Use this operation to report post processing errors related to consumed events.    This this generate and incident and it will require human intervention."""
        ...


    async def post_events_publishing_consents(
        self,
        consents_update_event: Annotated[Optional[ConsentsUpdateEvent], Field(description="Event to publish")],
    ) -> None:
        """Allows to publish an consent update event to all subscribing/consumer applications.  """
        ...


    async def post_events_publishing_pace(
        self,
        pace_update_event: Annotated[Optional[PaceUpdateEvent], Field(description="Event to publish")],
    ) -> None:
        """Allow to publish an PaCE update events to one or more subscribing/consumer applications."""
        ...
