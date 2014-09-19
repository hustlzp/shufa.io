import os
from shufa import create_app
from shufa.models import db


class BaseSuite(object):
    def setup(self):
        os.environ['MODE'] = 'TESTING'

        app = create_app()
        self.app = app

        self.client = app.test_client()

        with app.app_context():
            db.drop_all()
            db.create_all()

    def teardown(self):
        with self.app.app_context():
            db.drop_all()
