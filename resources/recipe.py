from flask import Flask, request
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipe_list

class RecipeListResource(Resource):
    def get(self):
        data = []  # data diawal masih kosong
        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)  # data diisi
        return {"data": data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()  # format JSON
        recipe = Recipe(  # pengecekan dengan model Recipe
            name=data["name"],
            description=data["description"],
            num_of_servings=data["num_of_servings"],
            cook_time=data["cook_time"],
            directions=data["directions"],
        )
        recipe.save()
        data = {"id": recipe.id, "name": recipe.name, "description": recipe.description, "num_of_servings": recipe.num_of_servings, "cook_time": recipe.cook_time, "directions": recipe.directions}
        return data, HTTPStatus.CREATED
        # recipe_list.append(recipe)  # mengisi recipe_list dengan data
        # return recipe.data, HTTPStatus.CREATED  # status created
        

class RecipeResource(Resource):
    def get(self, recipe_id):
        recipe = next (
            (
                recipe
                for recipe in recipe_list
                if recipe.id == recipe_id and recipe.is_publish == True
            ),
            None,
        )
        if recipe is None:
            return {"message" : "recipe not found"}, HTTPStatus.NOT_FOUND
        return recipe.data, HTTPStatus.OK
    
    def put(self, recipe_id):
        data = request.get_json()
        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id), None
        )
        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        
        recipe.name=data["name"]
        recipe.description=data["description"]
        recipe.num_of_servings=data["num_of_servings"]
        recipe.cook_time=data["cook_time"]
        recipe.directions=data["directions"]
        return recipe.data, HTTPStatus.OK 

class RecipePublishResource(Resource):
    def put(self, recipe_id):
        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id), None
        )
        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        recipe.is_publish = True
        return {}, HTTPStatus.NO_CONTENT
    def delete(self, recipe_id):
        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id), None
        )
        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        recipe.is_publish = True
        return {}, HTTPStatus.NO_CONTENT