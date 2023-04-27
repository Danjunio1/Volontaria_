from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail



# Create your models here.
class Abonne(models.Model):
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

class Categorie(models.Model):
    nom = models.CharField(max_length=30,unique=True)
    
class Tag(models.Model):
    nom = models.CharField(max_length=20,unique=True,)
    
class Article(models.Model):
    poster = models.FileField(upload_to='covers/')
    vue = models.IntegerField(default=0)
    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    titre = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag)
    contenu = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class Comment(models.Model):
    nom_auteur = models.CharField(max_length=20)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    contenu = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    
    

'''
@receiver(post_save, sender=Article)
def create_article(sender, instance=None, created=False, **kwargs):
    if created:
        #print(sender)
        abonnes = [ abonne.email for abonne in  Abonne.objects.all() ]
        send_mail(
    'Un Nouveau Article',
    f'Cette Semaine Nous avons ecris un article pour vous sur ce lien : http://localhost:8000/single-blog/{sender.id}',
    'stanjunior262@gmail.com',
    abonnes,
    fail_silently=False,
    )
'''
       