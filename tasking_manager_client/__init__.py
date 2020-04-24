"""HOTOSM Tasking Manager API client"""

__version__ = "0.0.1"


import requests
import json
import pandas as pd
from loguru import logger

DEFAULT_INSTANCE = 'tasks.hotosm.org'

def v1_project_search(textSearch="", mapperLevel='ALL', projectStatuses='', page = 1, token='', instance=DEFAULT_INSTANCE):

    # both must be empty, or both must be non-empty
    assert (projectStatuses == '') == (token == ''), "DRAFT and ARCHIVED require auth token"
    request_count = 0
    while True:

        r = requests.get(f"https://{instance}/api/v1/project/search",
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
        logger.debug(j.keys())
        assert r.status_code == 200, f"request failed: {j}"

        df = pd.DataFrame(j['results'])
        df['page'] = page

        yield df

        if j['pagination']['hasNext'] is True:
            page = j['pagination']['nextNum']
        else:
            break
