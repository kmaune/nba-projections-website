from flask import render_template, flash, session, request, redirect, url_for, Blueprint
from project import app, mysql, dbConnection
import pandas as pd

homepage_blueprint = Blueprint('homepage', '__name__', url_prefix='/')

@homepage_blueprint.route('/', methods=['POST', 'GET'])
@homepage_blueprint.route('/home', methods=['POST', 'GET'])
def homepage():
    df = pd.read_sql('SELECT * FROM Advanced_Stats', dbConnection)
    df.set_index(['Name'], inplace=True)
    df.index.name=None
    return render_template('homepage.html', data=df.to_html(classes='pandas'))
