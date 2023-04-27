from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.acceuil,name="acceuil"),
    path("qui-sommes-nous/", views.apropos,name="apropos"),
    #path("parrainage/", views.parrainage,name="parrainage"),
    #path("parrainage/", views.parrainage,name="parrainage"),
    path("nous-soutenir/", views.soutenir,name="soutenir"),
    #path("chantier/", views.chantier,name="chantier"),
    path("souscrire/", views.souscrire,name="souscrire"),
    path("stage/", views.stage,name="stage"),
    #path("tourisme/", views.tourisme,name="tourisme"),
    path("togo/", views.togo,name="togo"),
    
    path("tourisme/", views.tourisme, name="tourisme"),
    path('nous-contacter/', views.contacter, name='contacter'),
    path("Preparer-son-voyage/", views.voyager, name="voyager"),
    path("Vie-quotidienne/", views.vie, name="vie"),
    path("blog/", views.blog, name="blog"),
    path("login/", views.Login, name="login"),
    path("single-blog/<int:pk>", views.single_blog, name="single-blog"),
    path("modifier-blog/<int:pk>", views.modifier_blog, name="modifier-blog"),
    path("create-blog/", views.create_blog, name="create-blog"),
    path("create-categorie/", views.create_categorie, name="create-categorie"),
    path("modifier-categorie/<int:pk>", views.modifier_categorie, name="modifier-categorie")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
