from contextlib import redirect_stderr
from datetime import date, datetime
from pydoc import render_doc
from flask import jsonify

from flask import Blueprint, make_response, render_template, url_for, request, flash , Response
from flask import session
from itsdangerous import json

from sqlalchemy import true
from werkzeug.utils import redirect

from app.forms import AddressForm
from .function.map import get_location
bp = Blueprint('road', __name__, url_prefix='/road')

@bp.route('/', methods=('POST','GET'))
def road_input():
    form = AddressForm()
    if request.method == 'POST' and form.validate_on_submit():
        address_latlng = get_location(form.address.data)
        if not address_latlng:
            flash("주소를 다시 입력하세요.")
        else:
            lat, lng = address_latlng
            #return render_doc('road.html', form=form, lat=lat, lng=lng)
            return render_template('road2.html', form=form, lat=lat, lng=lng)

    return render_template('road.html', form=form)

@bp.route('/map')
def lat_lng_map():
    return jsonify(lat = request.args.get('lat', 123),
                   lng = request.args.get('lng', 30))

@bp.route('/map2')
def test():
    return render_template('inc/address_searchs.html')




def ymd(fmt):
    def trans(date_str):
        return datetime.strftime(date_str, fmt)
    return trans

@bp.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%y-%m-%d'))
    return "우리나라 "+ str(datestr)


@bp.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    session['Token'] = '123x'
    return make_response(res)