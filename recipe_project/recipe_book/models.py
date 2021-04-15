from django.db import models




class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    ingredients = models.TextField()
    how_to = models.TextField()
    type_food = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)