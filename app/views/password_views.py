from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.utils import redirect
from app import db
from app.forms import UserAuthenticPw, UserSearchPw
from app.models import User, PwGuest
from ..mail import email_auth_num,mail

bp = Blueprint('pw', __name__, url_prefix='/pw')


@bp.route('/pwsearch/', methods=('GET','POST'))
def idtest():
    form = UserSearchPw()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = '입력하신 정보가 올바르지 않습니다.'
        else:
            checkemail = (user.email==form.email.data)
            if not checkemail:
                error = '입력하신 정보가 올바르지 않습니다.'
            if error is None :
                pin_num = email_auth_num()
                mail(form.email.data, pin_num)
                # 메일 전송
                if PwGuest.query.filter(PwGuest.username==form.username.data).first() ==None:
                    pwguest = PwGuest(username=form.username.data, pin=pin_num)
                else: 
                    pwguest = PwGuest.query.filter(PwGuest.username==form.username.data).first()
                    pwguest.pin = pin_num
                db.session.add(pwguest)
                db.session.commit()
                return render_template('pw/pwauthentic.html', pwguest=pwguest, form=UserAuthenticPw())
            else :
                error = '입력하신 정보가 올바르지 않습니다.'
        flash(error)
    return render_template('pw/pwsearch.html', form=form)


@bp.route('/authentic_pin/<int:pwguest_id>', methods=('GET','POST'))
def authentic_pin(pwguest_id):
    form = UserAuthenticPw()
    pwguest = PwGuest.query.get_or_404(pwguest_id)
    if request.method == 'POST' and form.validate_on_submit():
        if pwguest.pin== form.pin.data:
            flash('testclear')
        else:
            flash("error")
    return render_template('pw/pwauthentic.html', pwguest=pwguest, form=UserAuthenticPw())