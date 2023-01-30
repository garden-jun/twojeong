from flask import Blueprint, render_template
from models import USER
from flask import request

# bp객체 생성 #__name__은 모듈명인 main_views가 전달된다.
bp = Blueprint('main', __name__, url_prefix='/')    #main은 blueprint의 "별칭"
                                                    #url_prefix는 라우팅함수의 애너테이션 URL앞에 기본으로 붙일 접두어 URL을 의미한다.

@bp.route('/', methods = ['GET', 'POST'])
def hello_pybo():

    user = USER.query()
    return render_template('main.html', USER = USER)

@bp.route('/2', methods = ['GET', 'POST'])
def hello_pybo2():
    temp = request.args.get("id", "abc")
    temp2 = request.args.get(2, "abcd")
    return temp + "-"+temp2