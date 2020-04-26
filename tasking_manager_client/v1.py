
import requests
import json
import pandas as pd
from loguru import logger

from tasking_manager_client import DEFAULT_INSTANCE


def project_search(textSearch="", mapperLevel='ALL', projectStatuses='', page = 1, token='', instance=DEFAULT_INSTANCE):

    # both must be empty, or both must be non-empty
    assert ('DRAFT' in projectStatuses) == ('Token' in token), "Searching DRAFTs requires auth token"
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
        assert r.status_code == 200, f"request failed: {j}"

        df = pd.DataFrame(j['results'])
        df['page'] = page

        yield df

        if j['pagination']['hasNext'] is True:
            page = j['pagination']['nextNum']
        else:
            break
