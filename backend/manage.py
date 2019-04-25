from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from application.app import create_app
from application.models import db, List, Item

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.shell
def shell_ctx():
	return dict(
		app = app,
		db = db,
		List = List,
		Item = Item
		)

if __name__ == '__main__':
	manager.run()