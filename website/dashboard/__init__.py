from flask import Flask
from dash import Dash

from config import DashConfig


def create_dash_application(app: Flask):
    with app.app_context():
        dash_app = Dash(
            server=app,
            name=DashConfig.SERVER_NAME,
            routes_pathname_prefix=DashConfig.ROUTES_PATHNAME_PREFIX,
            use_pages=DashConfig.USE_PAGES,
            pages_folder=DashConfig.PAGES_FOLDER,
            include_pages_meta=DashConfig.INCLUDE_PAGES_META,
            external_stylesheets=DashConfig.EXTERNAL_STYLESHEETS,
        )
        return dash_app
