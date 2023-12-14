from threading import Thread

from config import FlaskConfig
from website import create_flask_app
from website.scraper import run_scraper
from website.dashboard import create_dash_application


if __name__ == "__main__":
    # FLASK app
    app = create_flask_app()
    app.config.from_object(FlaskConfig)
    # DASH app
    create_dash_application(app)
    # SCRAPER
    scraper_thread = Thread(target=run_scraper, args=(app,)).start()

    app.run(host="0.0.0.0")
