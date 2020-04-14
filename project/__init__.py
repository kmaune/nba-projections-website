from flask import Flask, render_template, flash, session, request, redirect, url_for, Blueprint
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from db_setup.setup import *
from project.helper import *

app = Flask(__name__)

#Enable bootsrap
bootstrap = Bootstrap(app)

#Create/Initialize Database structure
#setup_db()

#Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'nba_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MySQL
mysql = MySQL(app)
#print(MySQL)
#From project.helper
#initialize(app, mysql);

from project.routes.homepage import homepage_blueprint

app.register_blueprint(homepage_blueprint)

#Don't think this ever gets called
@app.route('/')
def root():
    return redirect(url_for('/'))



