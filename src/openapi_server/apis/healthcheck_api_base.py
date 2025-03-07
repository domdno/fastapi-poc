# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.get_healthcheck200_response import GetHealthcheck200Response


class BaseHealthcheckApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseHealthcheckApi.subclasses = BaseHealthcheckApi.subclasses + (cls,)
    async def get_healthcheck(
        self,
    ) -> GetHealthcheck200Response:
        """The healthcheck confirms that everything is working!"""
        ...
