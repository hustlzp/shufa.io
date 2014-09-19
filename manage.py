# coding: utf-8
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from shufa import create_app
from shufa.models import db

# Used by app debug & livereload
PORT = 5000

app = create_app()
manager = Manager(app)

# db migrate commands
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    """Run app."""
    app.run(port=PORT)


@manager.command
def live():
    """Run livereload server"""
    from livereload import Server
    import formic

    server = Server(app)

    # css
    for filepath in formic.FileSet(include="shufa/static/css/**/*.css"):
        server.watch(filepath)
    # html
    for filepath in formic.FileSet(include="shufa/templates/css/**/*.html"):
        server.watch(filepath)
    # js
    for filepath in formic.FileSet(include="shufa/static/js/**/*.js"):
        server.watch(filepath)
    # image
    for filepath in formic.FileSet(include="shufa/static/image/**/*.*"):
        server.watch(filepath)

    server.serve(port=PORT)


@manager.command
def createdb():
    """Create database."""
    db.create_all()


if __name__ == "__main__":
    manager.run()