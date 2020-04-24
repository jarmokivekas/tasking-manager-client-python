
import pytest
import tasking_manager_client as tm
import pandas as pd

def test_v1_project_search():

    page1 = next(tm.v1_project_search(textSearch='covid'))
    assert isinstance(results, pd.DataFrame)
