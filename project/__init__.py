import pymysql
import pandas as pd
from flask import Flask, render_template, flash, session, request, redirect, url_for, Blueprint
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine 
from db_setup.setup import *
from project.helper import *

app = Flask(__name__)

#Enable bootsrap
bootstrap = Bootstrap(app)

#Create/Initialize Database structure
#FIX ME --- This should be uncommented before final commit, commented out to speed up start time of site for development since DB is already setup locally
#setup_db()

#Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'nba_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MySQL
mysql = MySQL(app)

sqlEngine = create_engine('mysql+pymysql://root:password@localhost/nba_db')
dbConnection = sqlEngine.connect()

#From project.helper
#FIX ME --- This should be uncommented before final commit, commented out to speed up start time of site for development since DB is already setup locally
#initialize(app, mysql);

from project.routes.homepage import homepage_blueprint
from project.routes.originalProject import originalProject_blueprint
from project.routes.aboutMe import aboutMe_blueprint

app.register_blueprint(homepage_blueprint)
app.register_blueprint(originalProject_blueprint)
app.register_blueprint(aboutMe_blueprint)

#Don't think this ever gets called
@app.route('/')
def root():
    return redirect(url_for('/'))



