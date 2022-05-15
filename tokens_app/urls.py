from django.urls import path
from . import views

urlpatterns = [
    path('', views.token_search, name='token_search'),
]
