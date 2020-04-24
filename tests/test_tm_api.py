
import vcr
import pytest
import tasking_manager_client as tm
import pandas as pd

@vcr.use_cassette()
def test_v1_project_search():

    page1 = next(tm.v1_project_search(textSearch='covid'))
    assert isinstance(page1, pd.DataFrame)
    assert isinstance(page1.status, pd.Series)
