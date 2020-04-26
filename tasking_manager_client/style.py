from matplotlib.colors import LinearSegmentedColormap
from tasking_manager_client import DEFAULT_INSTANCE

# colors from the HOTOSM media kit :)
hotosm_colors = {
  "red": "#D73F3F",
  "red-dark": "#6C2020",
  "red-light": "#FFEDED",
  "orange": "#FAA71E",
  "tan": "#F0EFEF",
  "blue-dark": "#2C3038",
  "blue-grey": "#68707F",
  "blue-light": "#929DB3",
  "grey-light": "#E1E0E0",
  "green": "#53AE62"
}


def hotosm_cmap():
    # create a colormap for colorign mappedness and validatedness percentages
    colors = [
        hotosm_colors['red'], hotosm_colors['orange'],
        hotosm_colors['green']
    ]
    colormap = LinearSegmentedColormap.from_list('hotosm-RdOrGr', colors, N=20)
    return colormap

def format_priority(val: str) -> str:
    """Pandas styler, set cell color based on project priority in TM.
    val: on of LOW, MEDIUM, HIGH, or URGENT"""
    lookup = {
        'LOW': hotosm_colors['grey-light'],
        'MEDIUM': hotosm_colors['green'],
        'HIGH': hotosm_colors['orange'],
        'URGENT': hotosm_colors['red']
    }
    color = lookup.get(val, "none")
    return f'background-color: {color};'


def format_status(val: str) -> str:
    """Pandas styler, set cell color based on proejct status in TM"""
    lookup = {
        'ARCHIVED': hotosm_colors['grey-light'],
        'PUBLISHED': hotosm_colors['green'],
        'DRAFT': hotosm_colors['orange']
    }
    color = lookup.get(val, "none")
    return f'background-color: {color};'


def format_project_link(id: int, instance=DEFAULT_INSTANCE) -> str:
    """Returns project URL for given project id.
    Defaults to main TM instance."""
    return f"https://{instance}/project/{id}"


def format_clickable_project_id(id: int, instance=DEFAULT_INSTANCE) -> str:
    """Returns a html link tag string linking to the project"""
    url = format_project_link(id, instance=instance)
    return f'<a href="{url}">{id}</a>'
