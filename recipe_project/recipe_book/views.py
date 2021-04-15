from django.shortcuts import render, redirect
from recipe_book.models import Recipe, Comment
from .forms import NewUserForm, RecipeForm, CommentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Main view where all recipes are present
def recipe_index(request):

    recipe_book = Recipe.objects.all()
    
    context = {
        'recipe_book': recipe_book
    }
    return render(request, 'recipe_index.html', context)

# Detailed view of any one single recipe
def recipe_detail(request, pk):

    recipe = Recipe.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user.username,
                body=form.cleaned_data["body"],
                recipe=recipe
            )
            comment.save()
            form =CommentForm()
    comments = Comment.objects.filter(recipe=recipe)
    context = {
        'recipe': recipe,
        'comments': comments,
        'form': form,
    }
    return render(request, 'recipe_detail.html', context)

# Register view
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("recipe_index")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request, "register.html", {"register_form": form})

# Login view
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("recipe_index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})

def logout_request(request):
    logout(request)
    return render(request, "logout.html")
# Recipe creation view
def recipe_form(request):

    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = Recipe(
                author=request.user.username,
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                ingredients=form.cleaned_data["ingredients"],
                how_to=form.cleaned_data["how_to"],
                type_food=form.cleaned_data["type_food"],
                
            )
            recipe.save()         
            return redirect('recipe_index')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form, })

# Creates the view where only the recipes for this user are present
def my_recipes(request):
    author = request.user.username
    recipe_book = Recipe.objects.filter(author=author)
    context = {
        'recipe_book': recipe_book
    }
    return render(request, 'my_recipes.html', context)
