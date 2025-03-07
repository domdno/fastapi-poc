# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Dict, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401


def test_post_prospects(client: TestClient):
    """Test case for post_prospects

    New Marketing signup
    """
    prospect_registration = {"prospect_id":"111000001100001","first_name":"firstName","last_name":"lastName","communications":[{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"},{"number":"7818626087","is_primary":1,"type":"homePhone","status":"active"}],"consents_and_preferences":[{"preferences":[{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]}],"name":"Patient Support Program Communications","status":"optOut"},{"preferences":[{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]},{"name":"bestContactTime","selected_options":["morning","morning","morning","morning","morning"]}],"name":"Patient Support Program Communications","status":"optOut"}],"address":{"city":"Lexington","country_code":"US","postal_code":"02420-5303","address_line1":"874 Massachusetts Avenue","address_line2":"addressLine2","state_or_province_code":"MA"},"marketing_campaign_source_code":"marketingCampaignSourceCode","survey":{"reason_to_register":"reasonToRegister","has_been_prescribed":"hasBeenPrescribed"},"data_provider_id":"dataProviderId","above18":1,"preferences_link_token":"preferencesLinkToken"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/prospects/{brand}".format(brand='brand_example'),
    #    headers=headers,
    #    json=prospect_registration,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

