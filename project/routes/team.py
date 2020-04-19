from flask import render_template, flash, session, request, redirect, url_for, Blueprint
from project import app, mysql, dbConnection
import pandas as pd

team_blueprint = Blueprint('team', '__name__', url_prefix='/team')

@team_blueprint.route('/', methods=['POST', 'GET'])
@team_blueprint.route('/<team_id>', methods=['POST', 'GET'])
def team(team_id=None):
    #If team is not input, go to homepage
    if team_id is None:
        return redirect(url_for('homepage.homepage'))
    
    roster_df = pd.read_sql(f'SELECT Name, Position, Experience FROM Players WHERE Team = "{team_id}"', dbConnection)
    return render_template('team.html', data=roster_df.to_html(index = False, classes=['pandas', 'stripe', 'row-border', 'cell-border',  'order-column']))
