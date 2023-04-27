from django.shortcuts import render
from main.models import *
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.POST)
        # print("SSSSSSSSSSSSSS")
        if user is not None:
            login(request, user)
            return redirect("/Administration/dashboard")
        # print("FAILED")

    return render(request, 'login.html')
 
    pass

def create_article(request):
    if request.method == 'POST':
        pass
    return render('create_article.html',{catgories:'categories'})


def liste_article(request):
    articles = Article.objects.all()
    return render('liste_article.html',{articles:'articles'})


def liste_categorie(request):
    categories = Categorie.objects.all()
    return render('liste_categorie.html',{categories:'categories'})

def create_categorie(request):
    if request.method == 'POST':
        pass
    return render('create_categorie.html')
