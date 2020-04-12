'''
Select Constants and MySQL queries utilized during database
creation and initialization
'''

create_teams_table = "CREATE TABLE Teams (Team varchar(10) NOT NULL, PRIMARY KEY(Team));"

create_players_table = """CREATE TABLE Players (
                        PlayerID Int NOT NULL, 
                        Name varchar(30) NOT NULL,
                        Team varchar(10) NOT NULL,
                        Position varchar(5) NOT NULL,
                        Experience Int NOT NULL,
                        PRIMARY KEY(PlayerID),
                        FOREIGN KEY(Team) REFERENCES Teams (Team)
                        );"""

create_pergame_table = """CREATE TABLE PerGame_Stats (
                        Name varchar(30) NOT NULL,
                        Team varchar(10) NOT NULL,
                        Season varchar(12) NOT NULL,
                        GP Int NOT NULL,
                        GS Int NOT NULL, 
                        MPG Double(3,1) NOT NULL, 
                        PPG Double(3,1) NOT NULL, 
                        APG Double(3,1) NOT NULL,
                        FG Double(3,1) NOT NULL, 
                        FGA Double(3,1) NOT NULL,
                        FG_Percent Double(4,3) NULL,
                        3P Double(3,1) NOT NULL,
                        3PA Double(3,1) NOT NULL,
                        3P_Percent Double(4,3) NULL,
                        eFG_Percent Double(4,3) NULL,
                        FT Double(3,1) NOT NULL,
                        FTA Double(3,1) NOT NULL,
                        FT_Percent Double(4,3) NULL,
                        ORB Double(3,1) NOT NULL,
                        DRB Double(3,1) NOT NULL,
                        STL Double(3,1) NOT NULL,
                        BLK Double(3,1) NOT NULL,
                        TOV Double(3,1) NOT NULL,
                        PF Double(3,1) NOT NULL, 
                        PRIMARY KEY(Name, Team, Season)
                        );"""

create_advanced_table = """CREATE TABLE Advanced_Stats (
                        Name varchar(30) NOT NULL,
                        Team varchar(10) NOT NULL,
                        Season varchar(12) NOT NULL,
                        GP Int NOT NULL,
                        MP Int NOT NULL,
                        PER Double(10,5) NOT NULL,
                        TS_Percent Double(4,3) NOT NULL,
                        3PAr Double(4,3) NOT NULL,
                        FTr Double(4,3) NOT NULL,
                        ORB_Percent Double(3,1) NOT NULL,
                        DRB_Percent Double(3,1) NOT NULL,
                        TRB_Percent Double(3,1) NOT NULL,
                        AST_Percent Double(3,1) NOT NULL,
                        STL_Percent Double(3,1) NOT NULL,
                        BLK_Percent Double(3,1) NOT NULL,
                        TOV_Percent Double(3,1) NOT NULL,
                        USG_Percent Double(3,1) NOT NULL,
                        OWS Double(3,1) NOT NULL,
                        DWS Double(3,1) NOT NULL,
                        WS Double(3,1) NOT NULL,
                        WS_Per48 Double(3,1) NOT NULL,
                        OBPM Double(3,1) NOT NULL,
                        DBPM Double(3,1) NOT NULL,
                        BPM Double(3,1) NOT NULL,
                        VORP Double(3,1) NOT NULL,
                        PRIMARY KEY(Name, Team, Season)
                        );"""

create_per100_table = """CREATE TABLE Per100_Stats(
                        Name varchar(30) NOT NULL,
                        Team varchar(10) NOT NULL,
                        Season varchar(12) NOT NULL,
                        GP Int NOT NULL,
                        MP Int NOT NULL,
                        PTS Double(3,1) NOT NULL,
                        AST Double(3,1) NOT NULL,
                        FG Double(3,1) NOT NULL,
                        FGA Double(3,1) NOT NULL,
                        FG_Percent Double(4,3) NULL,
                        3P Double(3,1) NOT NULL,
                        3PA Double(3,1) NOT NULL,
                        3P_Percent Double(4,3) NULL,
                        FT Double(3,1) NOT NULL,
                        FTA Double(3,1) NOT NULL,
                        FT_Percent Double(4,3) NULL,
                        ORB Double(3,1) NOT NULL,
                        DRB Double(3,1) NOT NULL,
                        STL Double(3,1) NOT NULL,
                        BLK Double(3,1) NOT NULL,
                        TOV Double(3,1) NOT NULL,
                        PF Double(3,1) NOT NULL,
                        ORtg Int Not NULL, 
                        DRtg Int Not NULL, 
                        PRIMARY KEY(Name, Team, Season)
                        );"""


