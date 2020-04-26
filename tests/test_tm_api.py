
import vcr
import pytest
import tasking_manager_client as tm
import pandas as pd

@vcr.use_cassette()
def test_v1_project_search_first_page():

    page1 = next(tm.v1.project_search(textSearch='covid'))
    assert isinstance(page1, pd.DataFrame)
    assert isinstance(page1.status, pd.Series)
    assert len(page1) >= 14


@vcr.use_cassette()
def test_v1_project_search_all():

    pages = pd.concat(tm.v1.project_search(textSearch='covid'))
    assert isinstance(pages, pd.DataFrame)
    assert isinstance(pages.status, pd.Series)
    assert len(pages) > 14
