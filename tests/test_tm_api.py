
import vcr
import pytest
import tasking_manager_client as tm
import pandas as pd


##########
## Tasking manager V4 (aka v2 api)
##########

@vcr.use_cassette()
def test_v2_projects_id_contributions_queries_day():
    j = tm.v2.projects_id_contributions_queries_day(
        id=8301,
        instance='tasking-manager-tm4-production-api.hotosm.org'
    )
    assert isinstance(j['stats'], list)

@vcr.use_cassette()
def test_v2_project_search_all():

    pages = pd.concat(tm.v2.project_search(dict(textSearch='covid')))
    assert isinstance(pages, pd.DataFrame)
    assert isinstance(pages.status, pd.Series)
    assert len(pages) > 14

@vcr.use_cassette()
def test_v2_project_search_first_page():

    page1 = next(tm.v2.project_search(dict(textSearch='covid')))
    assert isinstance(page1, pd.DataFrame)
    assert isinstance(page1.status, pd.Series)
    assert len(page1) <= 14

@vcr.use_cassette()
def test_v2_project_search_draft():

    page1 = next(tm.v2.project_search(dict(textSearch='covid', projectStatuses='' )))
    assert isinstance(page1, pd.DataFrame)
    assert isinstance(page1.status, pd.Series)
    assert len(page1) <= 14


# @vcr.use_cassette()
# def test_v2_project_search_draft_archive_published():
#     textSearch='covid'
#     projectStatuses='DRAFT,ARCHIVED,PUBLISHED'
#     result = pd.concat(
#         tm.v2.project_search(
#             textSearch=textSearch,
#             projectStatuses=projectStatuses
#         ),
#         ignore_index=True
#     );
