from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    #path("recipe/", views.recipe, name="recipe"),
    #path("add-recipe/", views.add_recipe, name="add_recipe"),
    #path("all-recipe/", views.all_recipe, name="all_recipe"),
    #path("delete-recipe/<int:recipe_id>/", views.delete_recipe, name="delete_recipe"),
    #path("update-recipe/<int:recipe_id>/", views.update_recipe, name="update_recipe"),
    #path("search-by-name/<str:name>/recipe/", views.search_by_name_recipe, name="search_by_name_recipe"),

    path("recipe-list/", views.recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_id>/", views.recipe, name="recipe"),

]
