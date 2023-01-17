from flask import Blueprint, render_template


# bp객체 생성 #__name__은 모듈명인 main_views가 전달된다.
bp = Blueprint('main', __name__, url_prefix='/')    #main은 blueprint의 "별칭"
                                                    #url_prefix는 라우팅함수의 애너테이션 URL앞에 기본으로 붙일 접두어 URL을 의미한다.

@bp.route('/')
def hello_pybo():
    return render_template('main.html')