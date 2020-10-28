"""API conveniece functions for calling the v1 API. API v1 is implemented by
Tasking Manager 3 instances"""

import requests
import json
import pandas as pd
from loguru import logger

from tasking_manager_client import DEFAULT_INSTANCE_API


def projects_id_contributions_queries_day(id:int, instance:str=DEFAULT_INSTANCE_API):
    """Get contributions by day on a project"""
    r = requests.get(
        f'https://{instance}/api/v2/projects/{id}/contributions/queries/day/',
        headers= {
            'Content-Type': 'application/json',
        }
    )
    j = r.json()
    assert r.status_code == 200, f"request failed: {j}"
    return j




def project_search(filters, page:int = 1, token:str='',
    instance:str=DEFAULT_INSTANCE_API):
    """Uses GET `/v2/projects/` search, generator of search result pages staring from `page`
    projectStatuses: one or both of ARCHIVED, DRAFT, separated by comma"""

    request_count = 0
    get_params = filters
    while True:
        get_params['page'] = page
        r = requests.get(f"https://{instance}/api/v2/projects/",
            params = get_params,
            headers = {
                'Accept-Language': '*',
                'Content-Type': 'application/json',
                'Authorization': token
            }
        )

        request_count += 1
        assert request_count < 100, "api search query stuck in loop"

        j = r.json()
        assert r.status_code == 200, f"request failed: {j}"

        df = pd.DataFrame(j['results'])
        df['page'] = page

        yield df

        if j['pagination']['hasNext'] is True:
            page = j['pagination']['nextNum']
        else:
            break
