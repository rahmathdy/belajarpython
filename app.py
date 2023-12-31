from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from extensions import db
from models.user import User
from models.recipe import Recipe
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource
from resources.user import *


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # mengakses connection ke database
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)
    api.add_resource(UserListResource, "/user")
    api.add_resource(RecipeListResource, "/recipes")
    api.add_resource(RecipeResource, "/recipes/<int:recipe_id>")
    api.add_resource(RecipePublishResource, "/recipes/<int:recipe_id>/publish")


if __name__ == "__main__":
    app = create_app()
    app.run()