from flask import render_template, flash, session, request, redirect, url_for, Blueprint
from project import app, mysql, dbConnection
import pandas as pd

start_blueprint = Blueprint('start', '__name__', url_prefix='/start')

@start_blueprint.route('/', methods=['POST', 'GET'])
def start():
    teams_df = pd.read_sql('SELECT * FROM Teams', dbConnection)
    teams = teams_df['Team'].tolist()
    return render_template('start.html', data=teams)
