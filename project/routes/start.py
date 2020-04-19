from flask import render_template, flash, session, request, redirect, url_for, Blueprint
from project import app, mysql, dbConnection
import pandas as pd

start_blueprint = Blueprint('start', '__name__', url_prefix='/start')

@start_blueprint.route('/', methods=['POST', 'GET'])
def start():
    df = pd.read_sql('SELECT * FROM Advanced_Stats WHERE Season = "2016-2017"', dbConnection)
    df.set_index(['Name'], inplace=True)
    df.index.name=None
    return render_template('start.html', data=df.to_html(classes=['pandas', 'stripe', 'row-border', 'cell-border',  'order-column']))
