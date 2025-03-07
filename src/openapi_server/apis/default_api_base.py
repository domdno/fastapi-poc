# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated

from openapi_server.models.consents_update_event import ConsentsUpdateEvent
from openapi_server.models.demographic_delete_event import DemographicDeleteEvent
from openapi_server.models.demographic_merge_event import DemographicMergeEvent
from openapi_server.models.demographic_un_merge_event import DemographicUnMergeEvent
from openapi_server.models.demographic_update_event import DemographicUpdateEvent
from openapi_server.models.enrollment_event import EnrollmentEvent
from openapi_server.models.pace_update_event import PaceUpdateEvent


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def brand_enrollment_created_post(
        self,
        enrollment_event: Annotated[Optional[EnrollmentEvent], Field(description="Brand enrollment create")],
    ) -> None:
        ...


    async def brand_enrollment_updated_post(
        self,
        enrollment_event: Annotated[Optional[EnrollmentEvent], Field(description="Brand enrollment update")],
    ) -> None:
        ...


    async def brand_pace_updated_post(
        self,
        pace_update_event: Annotated[Optional[PaceUpdateEvent], Field(description="PaCE update")],
    ) -> None:
        ...


    async def patient_consents_updated_post(
        self,
        consents_update_event: Annotated[Optional[ConsentsUpdateEvent], Field(description="Consent update")],
    ) -> None:
        ...


    async def patient_demographics_deleted_post(
        self,
        demographic_delete_event: Annotated[Optional[DemographicDeleteEvent], Field(description="Demographics delete")],
    ) -> None:
        ...


    async def patient_demographics_merged_post(
        self,
        demographic_merge_event: Annotated[Optional[DemographicMergeEvent], Field(description="Demographics merge")],
    ) -> None:
        ...


    async def patient_demographics_un_merged_post(
        self,
        demographic_un_merge_event: Annotated[Optional[DemographicUnMergeEvent], Field(description="Demographics unmerge")],
    ) -> None:
        ...


    async def patient_demographics_updated_post(
        self,
        demographic_update_event: Annotated[Optional[DemographicUpdateEvent], Field(description="Demographics update")],
    ) -> None:
        ...


    # async def prospect_consents_updated_post(
    #     self,
    #     consents_update_event: Annotated[Optional[], Field(description="Consent update")],
    # ) -> None:
    #     ...
