from flask import render_template, flash, session, request, redirect, url_for, Blueprint
from IPython import embed
from project import app
from new_website.datascraping.parsers import * 
from new_website.datascraping.nbaRosterScraper import *


homepage_blueprint = Blueprint('homepage', '__name__', url_prefix='/')

@homepage_blueprint.route('/', methods=['POST', 'GET'])
@homepage_blueprint.route('/home', methods=['POST', 'GET'])
def index():
    return 'This is working nicely'
