from app import app, db
from app.api import blueprint
from app.model import *
from flask_migrate import Migrate

# initialize sqlalchemy for db operation
migrate = Migrate(app=app, db=db)
# register all blueprints from api
app.register_blueprint(blueprint=blueprint)
