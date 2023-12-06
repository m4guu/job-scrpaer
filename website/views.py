from flask import Blueprint, render_template
from .database import get_all_jobs

views = Blueprint('views', __name__)

@views.route('/')
def jobs():
    return render_template('jobs.html', jobs = get_all_jobs())

@views.route('/statistics')
def statistics():
    return render_template('statistics.html')
