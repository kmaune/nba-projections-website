#CONSTANTS
BASE_URL = "https://www.basketball-reference.com"
BASE_TEAMS = ['ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 
'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']
BASE_SEASONS = ['2018-2019', '2017-2018', '2016-2017', '2015-2016', '2014-2015', '2013-2014', '2012-2013']
BASE_DRAFTS = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012']


#def create_sql_team():
#    return ""

def check_empty(val=""):
	if val == "":
		return "0.0"
	return val

def any_empty(params=[]):
	for param in params:
		if param == "":
			return True
	return False

	
def create_sql_player(params=[]):
    return """INSERT INTO Players(PlayerID, Name, Team, Position, Experience)
								VALUES  (%d, '%s', '%s', '%s', '%s')""" \
								% (params[0], params[1], params[2], params[3], params[4])

def create_sql_perGame(params=[]):
    return """INSERT INTO PerGame_Stats(Name, 
										Team, 
										Season, 
										GP,
										GS, 
										MPG, 
										PPG, 
										APG, 
										FG, 
										FGA, 
										FG_Percent, 
										3P, 
										3PA, 
										3P_Percent,
										eFG_Percent, 
										FT, 
										FTA, 
										FT_Percent,
										ORB, 
										DRB, 
										STL, 
										BLK, 
										TOV, 
										PF) 
				VALUES ('%s', '%s', '%s', %d, %d, %f, %f, %f,
						%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, 
						%f, %f, %f, %f, %f, %f)""" %\
										(params[0], 
										 params[1],
										 params[2],
										 params[3], 
										 params[4],
										 params[5],
										 params[6],
										 params[7],
										 params[8], 
										 params[9], 
										 params[10],
										 params[11], 
										 params[12], 
										 params[13],
										 params[14],
										 params[15],
										 params[16],
										 params[17],
										 params[18],
										 params[19],
										 params[20],
										 params[21],
										 params[22],
										 params[23])

def create_sql_advanced(params=[]):
	return """INSERT INTO Advanced_Stats(Name, 
										Team, 
										Season, 
										GP,
										MP, 
										PER, 
										TS_PERCENT, 
										3PAr, 
										FTr, 
										ORB_Percent, 
										DRB_Percent, 
										TRB_Percent, 
										AST_Percent, 
										STL_Percent,
										BLK_Percent, 
										TOV_Percent, 
										USG_Percent, 
										OWS,
										DWS, 
										WS, 
										WS_Per48, 
										OBPM, 
										DBPM, 
										BPM,
										VORP) 
				VALUES ('%s', '%s', '%s', %d, %d, %f, %f, %f,
						%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, 
						%f, %f, %f, %f, %f, %f, %f)""" %\
										(params[0], 
										 params[1],
										 params[2],
										 params[3], 
										 params[4],
										 params[5],
										 params[6],
										 params[7],
										 params[8], 
										 params[9], 
										 params[10],
										 params[11], 
										 params[12], 
										 params[13],
										 params[14],
										 params[15],
										 params[16],
										 params[17],
										 params[18],
										 params[19],
										 params[20],
										 params[21],
										 params[22],
										 params[23],
										 params[24])

def create_sql_per100(params=[]):
	return """INSERT INTO Per100_Stats(Name, 
										Team, 
										Season, 
										GP,
										MP, 
										PTS, 
										AST, 
										FG, 
										FGA, 
										FG_Percent, 
										3P, 
										3PA, 
										3P_Percent,
										FT, 
										FTA, 
										FT_Percent,
										ORB, 
										DRB, 
										STL, 
										BLK, 
										TOV, 
										PF,
										ORtg,
										DRtg) 
				VALUES ('%s', '%s', '%s', %d, %d, %f, %f, %f,
						%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, 
						%f, %f, %f, %f, %d, %d)""" %\
										(params[0], 
										 params[1],
										 params[2],
										 params[3], 
										 params[4],
										 params[5],
										 params[6],
										 params[7],
										 params[8], 
										 params[9], 
										 params[10],
										 params[11], 
										 params[12], 
										 params[13],
										 params[14],
										 params[15],
										 params[16],
										 params[17],
										 params[18],
										 params[19],
										 params[20],
										 params[21],
										 params[22],
										 params[23])

def create_sql_draftee(params=[]):
	return """INSERT INTO Drafts(Name, 
								 Team, 
								 Year, 
								 Pick,
								 NBA_Seasons) 
				VALUES ('%s', '%s', '%s', %d, %d)""" %\
								 (params[0], 
								  params[1],
								  params[2],
								  params[3], 
								  params[4])

