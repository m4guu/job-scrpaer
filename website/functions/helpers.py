import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from plotly.graph_objs import Figure

from ..database import get_all_jobs_boards


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error during request to {url}: {e}")
        # TODO: add error handling
        return None


def make_soup(job_board):
    html_content = get_html(job_board["url"])
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    # TODO: add error handling
    return None


def generate_todays_basic_statistics(today_jobs):
    # Create a dictionary to store the count for each job board
    job_board_counts = defaultdict(int)
    data = {"Job Board": [], "Job Count": []}
    # Count the number of jobs for each job board
    for job_posting in today_jobs:
        job_board_id = job_posting["job_board_id"]
        job_board_counts[job_board_id] += 1

    # Display the results
    for job_board in get_all_jobs_boards():
        job_board_id = job_board["_id"]
        job_board_name = job_board["name"]
        job_count = job_board_counts[job_board_id]
        data["Job Board"].append(job_board_name)
        data["Job Count"].append(job_count)

    return data


def apply_common_layout(fig: Figure):
    fig.update_layout(
        plot_bgcolor="#252529",  # Background color
        paper_bgcolor="#252529",  # Paper color (plot area)
        font=dict(color="rgb(255, 255, 245, 0.86)", size=16),  # Font color
    )

    fig.update_xaxes(gridcolor="#10b981")  # Set your desired grid color
    fig.update_yaxes(gridcolor="#10b981")  # Set your desired grid color
    return fig
