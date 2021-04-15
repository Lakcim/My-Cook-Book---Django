from django.urls import path
from recipe_book import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.recipe_index, name="recipe_index"),
    path("<int:pk>/", views.recipe_detail, name="recipe_detail"),\
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("recipe_form/", views.recipe_form, name="recipe_form"),
    path("my_recipes/", views.my_recipes, name="my_recipes"),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)