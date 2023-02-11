from flask import Blueprint, render_template
from models import *
from flask import request
from http import HTTPStatus

# bp객체 생성 #__name__은 모듈명인 main_views가 전달된다.
bp = Blueprint('main', __name__, url_prefix='/')    #main은 blueprint의 "별칭"
                                                    #url_prefix는 라우팅함수의 애너테이션 URL앞에 기본으로 붙일 접두어 URL을 의미한다.

@bp.route('/', methods = ['GET', 'POST'])
def hello_pybo():

    return main_page
    # return render_template('main.html', USER = USER)

@bp.route('/2', methods = ['GET'])
def hello_pybo2():
    ret = {"count": 2,
           "students": [
               {"name": "홍길동", "age": 30},
               {"name": "김나나", "age": 25}
           ]
           }
    return ret

@bp.route('/3', methods = ['POST'])
def hello_pybo3():
    print(request.is_json)
    data = request.get_json()  # 클라이언트로부터 json형식으로 데이터를 받는다.
    # data = { "x" : 345, "y" : 827 }     포스트맨에서 바디부분에 연결

    if 'x' not in data or 'y' not in data:
        return {'message': '파라미터 오류'}, HTTPStatus.BAD_REQUEST

    x = data['x']  # 파이썬 딕셔너리 형태에서 데이터 억세스 방법
    y = data['y']

    z = x + y

    ret = {'sum': z}  # 딕셔너리 형태로 돌려준다.

    return ret

@bp.route('/regi/<int:team_id>', methods=('POST'))
def team_register():
    tm = request.get_json()
    team = Team(
        title=tm['title'],
        target_personnel=tm['target_personnel']
    )
    db.session.add(team)
    db.session.commit()
    flash('Team DB is saved')

    return 0

@bp.route('/view/<int:team_id>')
def team_view():
    tm = Team.query.filter(Team.id == team_id).all()
    flash(tm)
    return tm