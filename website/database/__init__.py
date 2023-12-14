from flask import current_app, g
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy
from datetime import datetime

import pandas as pd


def get_db():
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = PyMongo(current_app).db
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


# JOB API
def get_all_jobs():
    try:
        # TODO: add pagination
        return list(db.jobs.find())
    except Exception as e:
        return e


def get_today_jobs():
    today_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    try:
        # TODO: add pagination
        return list(db.jobs.find({"scrape_date": {"$gte": today_date}}))
    except Exception as e:
        return e


def save_new_jobs(jobs):
    # TODO: modify it so that all offers are not accessed/downloaded [e.g. update(UPSERT)]
    # TODO: insert same jobs each day? how to prevent expired ads?
    try:
        existing_jobs = set(
            (job["job_title"], job["company"]) for job in get_all_jobs()
        )
        unique_jobs = [
            job
            for job in jobs
            if (job["job_title"], job["company"]) not in existing_jobs
        ]
        db.jobs.insert_many(unique_jobs)
        # db.jobs.insert_many(jobs)
    except Exception as e:
        return e


# JOB BOARDS
def get_all_jobs_boards():
    try:
        return list(db["job-boards"].find())
    except Exception as e:
        return e


# STATISTICS


def save_statistics(statistics_csv):
    try:
        db.statistics.insert_many(pd.read_csv(statistics_csv).to_dict("records"))
    except Exception as e:
        return e
