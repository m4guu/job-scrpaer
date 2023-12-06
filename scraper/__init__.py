import os
import json
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

from functions import make_soup
from scrapers import scrape_bulldog_job, scrape_pracuj_pl, scrape_the_protocol

# Load environment variables from .env
load_dotenv()
db_password = os.getenv("MONGODB_PWD")
db_user = os.getenv("MONGODB_USER")
db_collection = os.getenv("MONGODB_COLLECTION")

# !SCRAPER
# Load job_boards
def scrape_job_data():
    job_boards = json.load(open('data/job_boards.json'))
    jobs = []


    scraper_functions = {
        'PracujPL': scrape_pracuj_pl,
        'BulldogJob': scrape_bulldog_job,
        'the:protocol': scrape_the_protocol,
    }

    for job_board in job_boards:
        try:
            soup = make_soup(job_board)
            jobs.extend(scraper_functions.get(job_board['name'])(soup))
        except Exception as e:
            print(f"Error processing {job_board['name']}: {str(e)}")

    # Convert data to JSON
    json_data = [{"job":job, "link":link, "salary":salary, "company":company, "workplace":workplace} for job, link, salary, company, workplace in jobs ]

    # !MONGODB CONNECTION
    client = MongoClient(f'mongodb+srv://{db_user}:{db_password}@nextjs.dakai.mongodb.net/?retryWrites=true&w=majority')
    client.jobneo.jobs.insert_many(json_data)