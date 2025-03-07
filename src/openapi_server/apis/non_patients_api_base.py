# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated


class BaseNonPatientsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseNonPatientsApi.subclasses = BaseNonPatientsApi.subclasses + (cls,)
    async def post_prospects(
        self,
        brand: Annotated[StrictStr, Field(description="Brand Name")],
        prospect_registration: Optional[Dict[str, Any]],
    ) -> None:
        """Allows patients or general public to sign up to receive more (marketing) information about a Boehringer Ingelheim brand. """
        ...
