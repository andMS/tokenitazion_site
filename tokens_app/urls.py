from django.urls import path
from . import views

urlpatterns = [
    path('', views.token_search, name='token_search'),
    path('home/', views.token_search, name='token_search'),
    path('search_results/', views.search_results, name='search_results'),

    # Files
    path('files/', views.resources, name='resources'),
]
