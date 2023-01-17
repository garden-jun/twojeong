from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# import config

# 전역변수로 db, migrate 객체를 생성
db = SQLAlchemy()
migrate = Migrate()

# create_app은 플라스크 내부에서 정의된 함수명으로 다른 이름을 사용하면 정상적으로 동작하지 않는다.
def create_app():
    # app.py 라는 모듈이 실행되므로 __name__ 변수에는 pybo라는 문자열이 담긴다.
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')  # "환경 변수 APP_CONFIG_FILE에 정의된 파일을 환경 파일로 사용하겠다"는 의미이다.

    # ORM
    db.init_app(app)    # db를 app에 등록
    migrate.init_app(app, db)   # migrate를 app에 등록

    """
    blueprint 생성 이전 사용한 라우팅 함수
    # @app.route는 URL과 플라스크 코드를 매핑하는 데코레이터
    # / URL이 요청되면 플라스크는 hello_pybo 함수를 실행시킨다.
    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'
    """

    # 블루프린트
    from views import main_views
    app.register_blueprint(main_views.bp)   # main_views.bp 파일에 있는 블루프린트 객체 bp를 등록

    return app
