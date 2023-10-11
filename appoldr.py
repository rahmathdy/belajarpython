from flask import Flask, jsonify, request

from flask_restful import Api
from flask_migrate import Migrate
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource
from config import Config

app = Flask(__name__)
api = Api(app)

api.add_resource(RecipeListResource, "/recipes")
api.add_resource(RecipeResource, "/recipes/<int:recipe_id>")
api.add_resource(RecipePublishResource, "/recipes/<int:recipe_id>/publish")


@app.route("/")
def hello():
    return "Hello, Inixindo!"


if __name__ == "__main__":
    app.run(debug=True, port=5002)
