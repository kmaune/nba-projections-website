import os
from data_scraping.scraper import *

BASE_TEAMS = ['ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL',
'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']
BASE_SEASONS = ['2018-2019', '2017-2018', '2016-2017', '2015-2016', '2014-2015', '2013-2014', '2012-2013']
BASE_DRAFTS = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012']

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

def add_teams_toDB(app, mysql):
    with app.app_context():
        for team in BASE_TEAMS:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO Teams(team) values ('%s')" % (team))
        mysql.connection.commit()
    
def scrape_data(app, mysql):
    get_individual_rosters(app, mysql)
    for season in BASE_SEASONS:
        get_per_game_stats(app, mysql, season)
        get_advanced_stats(app, mysql, season)
        get_per_100_stats(app, mysql, season)
    for draft in BASE_DRAFTS:
        get_nba_drafts(app, mysql, draft)

def initialize(app, mysql):
    setup_data_folder()
    add_teams_toDB(app, mysql)
    scrape_data(app, mysql)
