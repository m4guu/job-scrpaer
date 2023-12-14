import time

from flask import Flask
from datetime import datetime

from ..functions import make_soup
from .scrapers import scrape_bulldog_job, scrape_pracuj_pl, scrape_the_protocol
from ..database import save_new_jobs, get_all_jobs_boards


# !SCRAPER
def scrape_job_data():
    # Load job_boards
    job_boards = get_all_jobs_boards()
    jobs = []

    scraper_functions = {
        "PracujPL": scrape_pracuj_pl,
        "BulldogJob": scrape_bulldog_job,
        "the:protocol": scrape_the_protocol,
    }

    for job_board in job_boards:
        try:
            soup = make_soup(job_board)
            jobs.extend(scraper_functions.get(job_board["name"])(soup, job_board))
        except Exception as e:
            # TODO: add error handling
            print(f"Error processing {job_board['name']}: {str(e)}")

    # Convert data to JSON
    json_data = [
        {
            "job_board_id": job_board_id,
            "job_title": job,
            "link": link,
            "salary": {
                "txt": salary[0],
                "bottom_monthly_range": salary[1],
                "upper_monthly_range": salary[2],
            },
            "company": company,
            "workplace": workplace,
            "scrape_date": datetime.now(),
        }
        for job_board_id, job, link, salary, company, workplace in jobs
    ]
    # Save jobs to db
    save_new_jobs(json_data)


def run_scraper(app: Flask):
    with app.app_context():
        while True:
            scrape_job_data()
            time.sleep(24 * 60 * 60)
