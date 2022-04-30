from django.urls import path
from .views import *
urlpatterns = [
    # path('', index, name='home'),
    path('', MainPageView.as_view(), name='home'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe'),
    path('add/', add_recipe, name='add'),
    path('update/<int:pk>/', update_recipe, name='update'),
    path('delete/<int:pk>/', DeleteRecipeView.as_view(), name='delete')
]