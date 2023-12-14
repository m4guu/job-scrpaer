import dash

from flask import Blueprint, render_template
from .database import get_today_jobs

views = Blueprint("views", __name__)
DASH_PAGES = dash.page_registry.values()


@views.context_processor
def inject_data():
    return dict(dash_pages=DASH_PAGES)


@views.route("/")
def jobs():
    return render_template("jobs.html", jobs=get_today_jobs())


@views.route("/<path>")
def statistics(path):
    for page in DASH_PAGES:
        if page["path"] == f"/{path}":
            return render_template("dashboards.html", dash_page=page)

    # If the path doesn't match any Dash page, you may want to handle this case
    return render_template("404.html"), 404
