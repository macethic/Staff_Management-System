from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os
from app import app, db
#app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

#if __name__ == '__main__':
#	        manager.run(host="0.0.0.0",port=int("80"),debug=True)


