from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import path


# Create your views here.

def recipe_list(request):
    if request.method == GET:
        recipe = Recipe.object.all()
        serializer = RecipeSerializer.



