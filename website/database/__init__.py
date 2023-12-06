from flask import current_app, g
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy

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
        return list(db.jobs.find())
    
    except Exception as e:
        return e