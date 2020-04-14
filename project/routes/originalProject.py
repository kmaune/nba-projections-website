
from flask import render_template, flash, session, request, redirect, url_for, Blueprint
from project import app, mysql
from IPython import embed

originalProject_blueprint = Blueprint('originalProject', '__name__', url_prefix='/original-project')

@originalProject_blueprint.route('/', methods=['POST', 'GET'])
def originalProject():
    return render_template('originalProject.html')
