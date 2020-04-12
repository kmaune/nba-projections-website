import MySQLdb
from db_setup.helper import *

class NBA_Database(object):
    def __init__(self, host='localhost', user='root', password='password'):
        self.db = MySQLdb.connect(host=host, user=user, passwd=password)
        self.cursor = self.db.cursor()
    
    def create_database(self, name='nba_db'):
        #Delete database if already present, to make so nothing is corrupted on setup
        self.cursor.execute("DROP database IF EXISTS %s" % (name))
        self.cursor.execute("CREATE database %s" % (name))
        self.cursor.execute("USE %s" % (name))
        self.cursor.execute("SET foreign_key_checks=1")

    def initialize_standard_tables(self):
        self.cursor.execute(create_teams_table)
        self.cursor.execute(create_players_table)
        self.cursor.execute(create_pergame_table)
        self.cursor.execute(create_advanced_table)
        self.cursor.execute(create_per100_table)


#Create/Structrue mysql db
def setup_db():
    nba_db = NBA_Database()
    nba_db.create_database()
    nba_db.initialize_standard_tables()

# Run script in standalone to create/Structure the mysql db
if __name__ == ('__main__'):
    nba_db = NBA_Database()
    nba_db.create_database()
    nba_db.initialize_standard_tables()
