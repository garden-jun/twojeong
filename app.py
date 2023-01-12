from flask import Flask

# app.py 라는 모듈이 실행되므로 __name__ 변수에는 pybo라는 문자열이 담긴다.
app = Flask(__name__)

# @app.route는 URL과 플라스크 코드를 매핑하는 데코레이터
# / URL이 요청되면 플라스크는 hello_pybo 함수를 실행시킨다.
@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'