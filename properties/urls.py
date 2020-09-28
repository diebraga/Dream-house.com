from django.urls import path
from .views import PropertiesView, PropertyView, SearchView


urlpatterns = [
    path('', PropertiesView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', PropertyView.as_view()),
]
