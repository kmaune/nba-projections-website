import requests
from bs4 import BeautifulSoup
from csv import writer
from itertools import zip_longest
from data_scraping.helper import *

def get_per_game_stats(app, mysql, season="2018-2019"):
	season_end_year = season.split("-")[1]

	url = "{BASE_URL}/leagues/NBA_{season_end_year}_per_game.html".format(
			BASE_URL = BASE_URL,
			season_end_year = season_end_year
		)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	players = soup.find_all(attrs={"data-stat": "player"})
	teams = soup.find_all(attrs={"data-stat": "team_id"})
	games = soup.find_all(attrs={"data-stat": "g"})
	games_started = soup.find_all(attrs={"data-stat": "gs"})
	minutes = soup.find_all(attrs={"data-stat": "mp_per_g"})
	points = soup.find_all(attrs={"data-stat": "pts_per_g"})
	assists = soup.find_all(attrs={"data-stat": "ast_per_g"})
	field_goals = soup.find_all(attrs={"data-stat": "fg_per_g"})
	fg_attempts = soup.find_all(attrs={"data-stat": "fga_per_g"})
	fg_pct = soup.find_all(attrs={"data-stat": "fg_pct"})
	threes = soup.find_all(attrs={"data-stat": "fg3_per_g"})
	three_attempts = soup.find_all(attrs={"data-stat": "fg3a_per_g"})
	three_pct = soup.find_all(attrs={"data-stat": "fg3_pct"})
	eFG_pct = soup.find_all(attrs={"data-stat": "efg_pct"})
	free_throws = soup.find_all(attrs={"data-stat": "ft_per_g"})
	ft_attemps = soup.find_all(attrs={"data-stat": "fta_per_g"})
	ft_pct = soup.find_all(attrs={"data-stat": "ft_pct"})
	offensive_rebounds = soup.find_all(attrs={"data-stat": "orb_per_g"})
	defensive_rebounds = soup.find_all(attrs={"data-stat": "drb_per_g"})
	steals = soup.find_all(attrs={"data-stat": "stl_per_g"})
	blocks = soup.find_all(attrs={"data-stat": "blk_per_g"})
	turnovers = soup.find_all(attrs={"data-stat": "tov_per_g"})
	personal_fouls = soup.find_all(attrs={"data-stat": "pf_per_g"})

	with app.app_context():
		cursor = mysql.connection.cursor()
		for (player, tm, g, gs, mpg, pts, ast, fg, fga, fgp, 
			tp, tpa, tpp, efg, ft, fta, ftp, orb, drb, stl, 
			blk, tov, pf) in zip_longest(players, teams, games, 
			games_started, minutes, points, assists, field_goals, 
			fg_attempts, fg_pct, threes, three_attempts, three_pct,
			eFG_pct, free_throws, ft_attemps, ft_pct, offensive_rebounds,
			defensive_rebounds, steals, blocks, turnovers, personal_fouls):

			if player.text == "Player":
				continue

			tppVal = check_empty(tpp.text)
			fgpVal = check_empty(fgp.text)
			ftpVal = check_empty(ftp.text)
			efgVal = check_empty(efg.text)
			playerName = player.text
			playerName = playerName.replace("'", "")
			params = [playerName, tm.text, season, int(g.text),int(gs.text),
					  float(mpg.text), float(pts.text), float(ast.text), 
					  float(fg.text), float(fga.text), float(fgpVal), 
					  float(tp.text), float(tpa.text), float(tppVal), 
					  float(efgVal), float(ft.text), float(fta.text), 
					  float(ftpVal), float(orb.text), float(drb.text), 
					  float(stl.text), float(blk.text), float(tov.text),
					  float(pf.text)]
			insert_perGame = create_sql_perGame(params)
			cursor.execute(insert_perGame)
		mysql.connection.commit()




	return

def get_advanced_stats(app, mysql, season="2018-2019"):
	season_end_year = season.split("-")[1]

	url = "{BASE_URL}/leagues/NBA_{season_end_year}_advanced.html".format(
		BASE_URL = BASE_URL,
		season_end_year = season_end_year
	)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')


	players = soup.find_all(attrs={"data-stat": "player"})
	teams = soup.find_all(attrs={"data-stat": "team_id"})
	games = soup.find_all(attrs={"data-stat": "g"})
	minutes = soup.find_all(attrs={"data-stat": "mp"})
	PERs = soup.find_all(attrs={"data-stat": "per"})
	ts_pct = soup.find_all(attrs={"data-stat": "ts_pct"})
	three_rates = soup.find_all(attrs={"data-stat": "fg3a_per_fga_pct"})
	ft_rates = soup.find_all(attrs={"data-stat": "fta_per_fga_pct"})
	orb_pct = soup.find_all(attrs={"data-stat": "orb_pct"})
	drb_pct = soup.find_all(attrs={"data-stat": "drb_pct"})
	trb_pct = soup.find_all(attrs={"data-stat": "trb_pct"})
	ast_pct = soup.find_all(attrs={"data-stat": "ast_pct"})
	stl_pct = soup.find_all(attrs={"data-stat": "stl_pct"})
	blk_pct = soup.find_all(attrs={"data-stat": "blk_pct"})
	tov_pct = soup.find_all(attrs={"data-stat": "tov_pct"})
	usg_pct = soup.find_all(attrs={"data-stat": "usg_pct"})
	offensive_winshares = soup.find_all(attrs={"data-stat": "ows"})
	defensive_winshares = soup.find_all(attrs={"data-stat": "dws"})
	winshares = soup.find_all(attrs={"data-stat": "ws"})
	winshares_per48 = soup.find_all(attrs={"data-stat": "ws_per_48"})	
	obpms = soup.find_all(attrs={"data-stat": "obpm"})
	dbpms = soup.find_all(attrs={"data-stat": "dbpm"})
	bpms = soup.find_all(attrs={"data-stat": "bpm"})
	vorps = soup.find_all(attrs={"data-stat": "vorp"})


	with app.app_context():
		cursor = mysql.connection.cursor()
		for (player, tm, g, mp, per, ts, tpar, ftr, orb, drb, trb, 
			ast, stl, blk, tov, usg, ows, dws, ws, ws_per, obpm,
			dbpm, bpm, vorp) in zip_longest(players, teams, games, 
			minutes, PERs, ts_pct, three_rates, ft_rates, orb_pct, 
			drb_pct, trb_pct, ast_pct, stl_pct, blk_pct, tov_pct, 
			usg_pct, offensive_winshares, defensive_winshares, 
			winshares, winshares_per48, obpms, dbpms, bpms, vorps):

			if player.text == 'Player':
				continue
			if any_empty([mp.text, per.text, ts.text, tpar.text, ftr.text, orb.text, usg.text, ws.text]):
				continue
			playerName = player.text
			playerName = playerName.replace("'", "")
			params = [playerName, tm.text, season, int(g.text), int(mp.text),
					  float(per.text), float(ts.text), float(tpar.text), 
					  float(ftr.text), float(orb.text), float(drb.text), 
					  float(trb.text), float(ast.text), float(stl.text), 
					  float(blk.text), float(tov.text), float(usg.text), 
					  float(ows.text), float(dws.text), float(ws.text),
					  float(ws_per.text), float(obpm.text), float(dbpm.text),
					  float(bpm.text), float(vorp.text)]
			insert_advanced = create_sql_advanced(params)
			cursor.execute(insert_advanced)

		mysql.connection.commit()



		return


def get_per_100_stats(app, mysql, season="2018-2019"):
	pass
	season_end_year = season.split("-")[1]

	url = "{BASE_URL}/leagues/NBA_{season_end_year}_per_poss.html".format(
			BASE_URL = BASE_URL,
			season_end_year = season_end_year
		)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	players = soup.find_all(attrs={"data-stat": "player"})
	teams = soup.find_all(attrs={"data-stat": "team_id"})
	games = soup.find_all(attrs={"data-stat": "g"})
	minutes = soup.find_all(attrs={"data-stat": "mp"})
	points = soup.find_all(attrs={"data-stat": "pts_per_poss"})
	assists = soup.find_all(attrs={"data-stat": "ast_per_poss"})
	field_goals = soup.find_all(attrs={"data-stat": "fg_per_poss"})
	fg_attempts = soup.find_all(attrs={"data-stat": "fga_per_poss"})
	fg_pct = soup.find_all(attrs={"data-stat": "fg_pct"})
	threes = soup.find_all(attrs={"data-stat": "fg3_per_poss"})
	three_attempts = soup.find_all(attrs={"data-stat": "fg3a_per_poss"})
	three_pct = soup.find_all(attrs={"data-stat": "fg3_pct"})
	free_throws = soup.find_all(attrs={"data-stat": "ft_per_poss"})
	ft_attemps = soup.find_all(attrs={"data-stat": "fta_per_poss"})
	ft_pct = soup.find_all(attrs={"data-stat": "ft_pct"})
	offensive_rebounds = soup.find_all(attrs={"data-stat": "orb_per_poss"})
	defensive_rebounds = soup.find_all(attrs={"data-stat": "drb_per_poss"})
	steals = soup.find_all(attrs={"data-stat": "stl_per_poss"})
	blocks = soup.find_all(attrs={"data-stat": "blk_per_poss"})
	turnovers = soup.find_all(attrs={"data-stat": "tov_per_poss"})
	personal_fouls = soup.find_all(attrs={"data-stat": "pf_per_poss"})
	ortgs = soup.find_all(attrs={"data-stat": "off_rtg"})
	drtgs = soup.find_all(attrs={"data-stat": "def_rtg"})

	with app.app_context():
		cursor = mysql.connection.cursor()
		for (player, tm, g, mp, pts, ast, fg, fga, fgp, 
			tp, tpa, tpp, ft, fta, ftp, orb, drb, stl, 
			blk, tov, pf, ortg, drtg) in zip_longest(players,
			teams, games, minutes, points, assists, field_goals, 
			fg_attempts, fg_pct, threes, three_attempts, three_pct,
			free_throws, ft_attemps, ft_pct, offensive_rebounds, 
			defensive_rebounds, steals, blocks, turnovers, 
			personal_fouls, ortgs, drtgs):

			tppVal = check_empty(tpp.text)
			ftpVal = check_empty(ftp.text)
			fgpVal = check_empty(fgp.text)
			if player.text == 'Player':
				continue
			if any_empty([ortg.text, drtg.text]):
				continue
			playerName = player.text
			playerName = playerName.replace("'", "")
			params = [playerName, tm.text, season, int(g.text), int(mp.text), 
					  float(pts.text), float(ast.text), float(fg.text), 
					  float(fga.text), float(fgpVal), float(tp.text), 
					  float(tpa.text), float(tppVal), float(ft.text),
					  float(fta.text), float(ftpVal), float(orb.text), 
					  float(drb.text), float(stl.text), float(blk.text), 
					  float(tov.text), float(pf.text), int(ortg.text), int(drtg.text)]
			insert_per100 = create_sql_per100(params)
			cursor.execute(insert_per100)

		mysql.connection.commit()

	return


def get_nba_drafts(app, mysql, year='2018'):
	url = "{BASE_URL}/draft/NBA_{year}.html".format(
			BASE_URL = BASE_URL,
			year = year
		)

	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'html.parser')

	picks = soup.find_all(attrs={'data-stat': 'pick_overall'})
	teams = soup.find_all(attrs={'data-stat': 'team_id'})
	players = soup.find_all(attrs={'data-stat': 'player'})
	years = soup.find_all(attrs={'data-stat': 'seasons'})

	with app.app_context():
		cursor = mysql.connection.cursor()
		for pick, team, player, experience in zip_longest(picks, teams, players, years):
			expVal = experience.text
			if expVal == "":
				expVal = "0"
			if player.text == 'Player':
				continue
			playerName = player.text
			playerName = playerName.replace("'", "")
			insert_draftee = create_sql_draftee([playerName, team.text, year, 
												int(pick.text), int(expVal)])
			cursor.execute(insert_draftee)
		mysql.connection.commit()

	return 

def get_individual_rosters(app, mysql, teams=BASE_TEAMS):
	playerID = 1
	with app.app_context():
		cursor = mysql.connection.cursor()
		for team in teams:
			link_head = 'https://www.basketball-reference.com/teams/'
			link_end = '/2020.html'
			link = link_head + team + link_end
			#print(link)

			response = requests.get(link)

			soup = BeautifulSoup(response.text, 'html.parser')

			players = soup.find_all(attrs={"data-stat": "player"})
			positions = soup.find_all(attrs={"data-stat": "pos"})
			years_experience = soup.find_all(attrs={"data-stat": "years_experience"})

			for player, position, experience in zip_longest(players, positions, years_experience):
				if player.text == "Player":
					continue
				playerName = player.text
				playerName = playerName.replace("'", "")
				insert_player = create_sql_player([playerID, playerName, team, position.text, experience.text])
				cursor.execute(insert_player)
				playerID += 1
			mysql.connection.commit()
	return











