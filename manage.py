from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db


migrate = Migrate(app, db)

manage = Manager(app, db)
manage.add_command("db", MigrateCommand)


if __name__ == "__main__":
	manage.run()
