from flask import render_template, flash, session, request, redirect, url_for, Blueprint

homepage_blueprint = Blueprint('homepage', '__name__', url_prefix='/')

@homepage_blueprint.route('/', methods=['POST', 'GET'])
@homepage_blueprint.route('/home', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        return redirect(url_for('start.start'))
    return render_template('homepage.html')
