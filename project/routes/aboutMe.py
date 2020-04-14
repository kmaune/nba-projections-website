
from flask import render_template, flash, session, request, redirect, url_for, Blueprint

aboutMe_blueprint = Blueprint('aboutMe', '__name__', url_prefix='/about')

@aboutMe_blueprint.route('/', methods=['POST', 'GET'])
def aboutMe():
    return render_template('aboutMe.html')
