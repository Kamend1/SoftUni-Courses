from django.urls import path, include
from TastyRecipesAppExamPrep17042024.recipes import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.RecipeCreateView.as_view(), name='create-recipe'),
    path('<int:pk>/', include([
        path('details/', views.RecipeDetailsView.as_view(), name='details-recipe'),
        path('edit/', views.RecipeUpdateView.as_view(), name='edit-recipe'),
        path('delete/', views.RecipeDeleteView.as_view(), name='delete-recipe'),
    ]))
]
