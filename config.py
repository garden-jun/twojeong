import os

BASE_DIR = os.path.dirname(__file__)

# 데이터 베이스 접속주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy의 이벤트를 처리 하는 옵션

