# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.healthcheck_api_base import BaseHealthcheckApi
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
from openapi_server.models.get_healthcheck200_response import GetHealthcheck200Response


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/healthcheck",
    responses={
        200: {"model": GetHealthcheck200Response, "description": "OK"},
    },
    tags=["Healthcheck"],
    summary="Healthcheck",
    response_model_by_alias=True,
)
async def get_healthcheck(
) -> GetHealthcheck200Response:
    """The healthcheck confirms that everything is working!"""
    if not BaseHealthcheckApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseHealthcheckApi.subclasses[0]().get_healthcheck()
