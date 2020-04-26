

import tasking_manager_client as tm
import pytest

def test_color():
    help(tm)
    assert isinstance(tm.style.hotosm_colors, dict)

@pytest.mark.parametrize("status,color", [
    ("FOOBAR", 'none'),
    ("PUBLISHED", tm.style.hotosm_colors['green']),
    ("ARCHIVED", tm.style.hotosm_colors['grey-light']),
    ("DRAFT", tm.style.hotosm_colors['orange']),
])

def test_format_status(status,color):

    assert color in tm.style.format_status(status)
    assert "background-color" in tm.style.format_status(status)
    assert ":" in tm.style.format_status(status)
    assert ";" in tm.style.format_status(status)
