from flask import Flask, render_template, flash, session, request, redirect, url_for, Blueprint
from flask_mysqldb import MySQL

app = Flask(__name__)

from project.routes.homepage import homepage_blueprint

app.register_blueprint(homepage_blueprint)

@app.route('/')
def root():
    return redirect(url_for('/'))



