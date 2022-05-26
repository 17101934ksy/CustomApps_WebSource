from flask import Blueprint, render_template, url_for, render_template, Markup
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')
#블루 프린트 객체 생성 

@bp.route('/home')
def home():
    return render_template('main.html')

@bp.route('/')
def index():
    return redirect(url_for('main.home'))
