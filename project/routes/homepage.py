from flask import render_template, flash, session, request, redirect, url_for, Blueprint
from IPython import embed
from project import app, mysql
from data_scraping.scraper import *
import os
import errno

homepage_blueprint = Blueprint('homepage', '__name__', url_prefix='/')
intialized = False

@homepage_blueprint.route('/', methods=['POST', 'GET'])
@homepage_blueprint.route('/home', methods=['POST', 'GET'])
def homepage():
    return 'Database is setup'
