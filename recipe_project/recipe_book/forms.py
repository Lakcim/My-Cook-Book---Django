from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe

# Registration Form
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Coment Form
class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

# Recipe creation form
class RecipeForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Recipe Name"
        })
    )
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Add a short product description here."
        })
    )
    ingredients = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Add ingredient(seperate them with ',')"
        })
    )
    how_to = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Please explain how to create the product."
        })
    )
    type_food = forms.CharField(
        max_length=60,
		
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Type of food"
        })
    )

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'ingredients',
                  'how_to', 'type_food')
