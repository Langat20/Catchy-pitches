from app import db, create_app
from flask_migrate import Migrate
from flask_script import Manager,Server
from app.models import User,Role,Comments,Pitches
from  flask_migrate import Migrate, MigrateCommand


app = create_app('production')
manager = Manager(app)
migrate = Migrate(app,db)


manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell # helps us to create the shell context
def make_shell_context():# to allow us pass in some properties into our shell.
    return dict(app = app,db = db,User = User,Role = Role ,Pitches=Pitches,Comments=Comments)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
    
    
    
# @manager.shell
# def make_shell_context():
#     return dict(app=app,db=db,User = User, Role = Role, Comments=Comments, Pitches=Pitches)


if __name__ == '__main__':
    manager.run()