from contextlib import redirect_stderr
from datetime import date, datetime
from pydoc import render_doc
from flask import jsonify

from flask import Blueprint, make_response, render_template, url_for, request, flash , Response
from flask import session
from itsdangerous import json

from sqlalchemy import true
from werkzeug.utils import redirect

bp = Blueprint('client', __name__, url_prefix='/client')

@bp.route('/', methods=('POST','GET'))
def main():
    return render_template('client.html')
