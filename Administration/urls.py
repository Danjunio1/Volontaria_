from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.login,name='login'),
    path("login/",views.create_article,name='create_article'),
    path("create_article/",views.create_article,name='create_article'),
    path("create_categorie/",views.create_categorie,name='create_categorie'),
    path("liste_article/",views.liste_article,name='liste_article'),
    path("liste_categorie/",views.liste_categorie,name='liste_categorie')
    
]
