import os
import configparser
from enum import Enum


class Environment(Enum):
    DEV = "DEV"
    PROD = "PROD"


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


# FLASK APP CONFIG
class FlaskConfig:
    SECRET_KEY = config[Environment.DEV.value]["SECRET_KEY"]
    MONGO_URI = config[Environment.DEV.value]["DB_URI"]
    DEBUG = False


# DASH APP CONFIG
class DashConfig:
    SERVER_NAME = "Statistics"
    ROUTES_PATHNAME_PREFIX = "/dash/"
    USE_PAGES = True
    PAGES_FOLDER = "website/dashboard/pages"
    INCLUDE_PAGES_META = False
    EXTERNAL_STYLESHEETS = [{"href": "/static/css/index.css", "rel": "stylesheet"}]
