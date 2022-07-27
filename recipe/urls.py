from django.urls import path

from recipe.views import Contato, Home, Sobre

urlpatterns = [
    path('', Home),  # Home
    path('sobre/', Sobre),  # /Sobre/
    path('contato/', Contato),  # /COntato/


]
