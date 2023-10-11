from flask import Flask, jsonify, request
from http import HTTPStatus


app = Flask(__name__)

recipes = [
    {
        "id": 1,
        "name": "Egg Salad",
        "description": "This is a delicious egg salad recipe.",
    },
    {
        "id": 2,
        "name": "Tomato Pasta",
        "description": "This is a lovely tomato recipe.",
    },
]


# menampilkan seluruh data
@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify({"data": recipes})


# menampilkan sebagian data berdasarkan id
@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)

    if recipe:
        return jsonify(recipe)

    return jsonify({"message": "recipe non found"}), HTTPStatus.NOT_FOUND


# membuat data baru
@app.route("/recipes", methods=["POST"])
def create_recipe():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")

    recipe = {"id": len(recipes) + 1, "name": name, "description": description}
    recipes.append(recipe)

    return jsonify(recipe), HTTPStatus.CREATED


@app.route("/")
def hello():
    return "Hello, Inixindo!"


if __name__ == "__main__":
    app.run(debug=True, port=5002)
