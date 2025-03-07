# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.error_default import ErrorDefault
from openapi_server.models.flex_enrollment import FlexEnrollment
from openapi_server.security_api import get_token_oauth2DEV

class BaseEnrollmentApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEnrollmentApi.subclasses = BaseEnrollmentApi.subclasses + (cls,)
    async def post_patient_brand_enrollment(
        self,
        brand: Annotated[StrictStr, Field(description="Brand Name")],
        flex_enrollment: Annotated[Optional[FlexEnrollment], Field(description="Patient's details and enrollment  preferences (patient demographic, consents and clinical information).")],
    ) -> FlexEnrollment:
        """Allows to enroll a new patient to BI. Patient will be enrolled in the specified brand by providing their contact information, consents and subscriptions to services offered by BI (through its partners).  If the patient is found to be already register in BI, their demographic information will be updated along with any non-brand specific consents (i.e., BI Corporate Communications).  """
        ...


    async def post_patient_enroll_brand_async(
        self,
        brand: Annotated[StrictStr, Field(description="Brand Name")],
        flex_enrollment: Annotated[Optional[FlexEnrollment], Field(description="Patient's details and enrollment  preferences (patient demographic, consents and clinical information).  ")],
    ) -> None:
        """Allows to submit a patient information for enrollment to a BI brand. The patient could be existing or new.   Depending on the accuracy of the data provided, the enrollment could be done near real time or might require additional manual processing to complete the patient enrollment. """
        ...


    async def put_patient_brand_enrollment(
        self,
        id: Annotated[StrictStr, Field(description="BI's Patient Identifier")],
        brand: Annotated[StrictStr, Field(description="Brand Name")],
        flex_enrollment: Annotated[Optional[FlexEnrollment], Field(description="Patient's details and enrollment  preferences (patient demographic, consents and clinical information).")],
    ) -> FlexEnrollment:
        """Allows to enroll an existing patient in a new BI’ HP brand or update their enrollment to a brand.  The patient will be enrolled, or their enrollment will be updated, by providing their consents and subscriptions to services offered by BI (through its partners).  BI’s patient demographic information will also be updated with the data provided and it will be distributed to any other brands where the patient could have previously enrolled.  Client applications are expected to provide the latest patient demographic available to them to any means. """
        ...
