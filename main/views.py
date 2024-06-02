from django.http import HttpResponse, JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from main.models import Recipe
from main.serializers import RecipeSerializer


#########################
###############################

@swagger_auto_schema(methods=['POST'], request_body=RecipeSerializer)
@api_view(['GET', 'POST'])
def recipe_list(request):
    if request.method == "GET":
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        #data = JSONParser().parse(request)
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("here aa")
            return JsonResponse(serializer.data, status=201)
        print("here bb")
        return JsonResponse(serializer.errors, status=400)


    else:
        pass


@swagger_auto_schema(methods=['PUT', "DELETE"], request_body=RecipeSerializer)
@api_view(['GET', 'PUT', "DELETE"])
def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)

    except:
        return JsonResponse({"error": "recipe not found"}, status=400)

    if request.method == "GET":
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        #data = JSONParser().parse(request)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == "DELETE":
        recipe.delete()
        return HttpResponse(status=201)


    else:
        pass

################################
#########################################

#@api_view(['GET'])
#def recipe(request):
#    if request.method == 'GET':
#        data = {
#            "status": True,
#            "message": "RECIPE API",
#            "status_code": 201,
#        }
#        return Response(data)


#@api_view(['POST'])
#def add_recipe(request):
#    if request.method == 'POST':
#        name = request.data["name"]
#        detail = request.data["detail"]
#        ingredients = request.data["ingredients"]
#        tags = request.data["tags"]

#        recipe = Recipe.objects.create(name=name, detail=detail, ingredients=ingredients, tags=tags)
#        recipe.save()


#        data = {
#            "status": True,
#            "message": "Add recipe was successful",
#            "status_code": 201,
#            "id": recipe.id
#        }
#        return Response(data)


#@api_view(['GET'])
#def all_recipe(request):
#    if request.method == 'GET':

#       recipes = Recipe.objects.all()

#      final_recipes = []
#     for item in recipes:
#       new_obj = {
#            "id": item.id,
#          "name": item.name,
#         "detail": item.detail,
#        "ingredients": item.ingredients,
#   "tags": item.tags,
#    }

#
