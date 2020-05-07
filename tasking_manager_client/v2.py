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



# with vcr.use_cassette('tests/fixtures/notebooks.yaml'):




def project_search(textSearch:str="", mapperLevel:str='ALL', projectStatuses:str='', page:int = 1, token:str='', instance:str=DEFAULT_INSTANCE_API):
    """Uses GET v1/project/search, generator of search result pages staring from `page`
    projectStatuses: one or both of ARCHIVED, DRAFT, separated by comma"""
    # both must be empty, or both must be non-empty
    assert mapperLevel in ['BEGINNER', 'INTERMEDIATE', 'ADVANCED', 'ALL'], "invalid mapper category"
    # assert ('DRAFT' in projectStatuses) == ('Token' in token), "Searching DRAFTs requires auth token"
    request_count = 0
    while True:

        r = requests.get(f"https://{instance}/api/v2/projects/",
            params = {
                'textSearch': textSearch,
                'mapperLevel': mapperLevel,
                'projectStatuses': projectStatuses,
                'page': page
            },
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
