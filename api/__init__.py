from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource

def create_app():
  app = Flask(__name__)
  CORS(app)

  app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

  from .views import main
  app.register_blueprint(main)

  return app

# pipenv shell
# export FLASK_APP=api
# export FLASK_DEBUG=1
# flask run

