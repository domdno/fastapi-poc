# coding: utf-8

"""
    Patient Engagement Enterprise API

    Patient Engagement Enterprise API allows multiple communication channels (e.g. websites,  HUbs, etc.) to enrroll and/or manage patient's support porgrams and services offered by Boehringer Ingelheim brands.  

    The version of the OpenAPI document: 0.7.1
    Contact: zzITEDPPatientEngagementIntegration@boehringer-ingelheim.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from openapi_server.apis.default_api import router as EventConsumerRouter
from openapi_server.apis.consent_api import router as ConsentApiRouter
from openapi_server.apis.demographic_api import router as DemographicApiRouter
from openapi_server.apis.enrollment_api import router as EnrollmentApiRouter
from openapi_server.apis.events_api import router as EventsApiRouter
from openapi_server.apis.healthcheck_api import router as HealthcheckApiRouter
from openapi_server.apis.non_patients_api import router as NonPatientsApiRouter
from openapi_server.apis.pa_ce_api import router as PaCEApiRouter

app = FastAPI(
    title="Patient Engagement Enterprise API",
    description="Patient Engagement Enterprise API allows multiple communication channels (e.g. websites,  HUbs, etc.) to enrroll and/or manage patient&#39;s support porgrams and services offered by Boehringer Ingelheim brands.  ",
    version="0.7.1",
)

app.include_router(EventConsumerRouter)
app.include_router(ConsentApiRouter)
app.include_router(DemographicApiRouter)
app.include_router(EnrollmentApiRouter)
app.include_router(EventsApiRouter)
app.include_router(HealthcheckApiRouter)
app.include_router(NonPatientsApiRouter)
app.include_router(PaCEApiRouter)
