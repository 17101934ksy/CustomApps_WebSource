import smtplib
from email.mime.text import MIMEText
import string
import random

# email 검증 번호 생성
def email_auth_num():
    LENGTH=8
    string_pool=string.ascii_letters + string.digits
    auth_num=""
    for _ in range(LENGTH):
        auth_num += random.choice(string_pool)
    return auth_num

def mail(email, num):
    s= smtplib.SMTP('smtp.gmail.com',587)
    # 세션 초기화
    s.starttls()
    # TLS 보안
    s.login('')

    msg=MIMEText("임시 비밀번호 : "+ str(num))
    msg['Subject']='test : 임시 비밀번호'

    s.sendmail('', email, msg.as_string())
    s.quit()
    