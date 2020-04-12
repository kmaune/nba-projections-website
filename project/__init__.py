from flask import Flask, render_template, flash, session, request, redirect, url_for, Blueprint
from flask_mysqldb import MySQL
from db_setup.setup import *
app = Flask(__name__)

#Configure MySQL
app.config['MYSQL_HOST'] = 'locallhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'nba_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MySQL
mysql = MySQL(app)

from project.routes.homepage import homepage_blueprint

app.register_blueprint(homepage_blueprint)

def setup_data_folder():
    filepath='data/rosters/'
    if not os.path.exists(os.path.dirname(filepath)):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    filepath='data/player_stats/'
    if not os.path.exists(os.path.dirname(filepath)):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    filepath='data/drafts/'
    if not os.path.exists(os.path.dirname(filepath)):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

def scrape_data():
    get_individual_rosters()

@app.route('/')
def root():
    setup_data_folder()
    setup_db()
    scrape_data()
    return redirect(url_for('/'))



