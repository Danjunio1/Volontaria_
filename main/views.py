from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate, logout, decorators
from django.core.files.storage import FileSystemStorage
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator
import datetime


# Create your views here.

def acceuil(request):
    
    articles = Article.objects.all().order_by('-created')[:3]
    
    return render(request,'acceuil.html',{'articles':articles})



def apropos(request):
    return render(request,'apropos.html')


def parrainage(request):
    return render(request,'parrainage.html')


def soutenir(request):
    return render(request,'soutenir.html')

def chantier(request):
    return render(request,'chantier.html')


def stage(request):
    return render(request,'stage.html')

#def tourisme(request):
#    return render(request,'tourisme.html')

def togo(request):
    return render(request,'togo.html')


#########DAN

def tourisme(request):
    return render(request, 'tourisme.html')


def voyager(request):
    return render(request, 'voyager.html')


def vie(request):
    return render(request, 'vie.html')

def contacter(request):
    return render(request, 'contacter.html')

def souscrire(request):
    if request.method == 'POST':
        Abonne.objects.create(email=request.POST['email'])
    return redirect('/')


def blog(request):
    articles = Article.objects.order_by('-created')
    articles_recent = Article.objects.order_by('-created')[:5]
    categories = Categorie.objects.all()
    tags = Tag.objects.all()
    print(request.GET)
    paginator = Paginator(articles, 9)
    page_number = 1
    
    try:
        page_number = request.GET.get("page")
        
        query = request.GET['query']
        articles = Article.objects.filter(titre__icontains=query).order_by('-created')
    except Exception as e:
        print(e)


    
    try:
        categorie = Categorie.objects.get(pk=int(request.GET['categorie']))
        articles = Article.objects.filter(categorie=categorie).order_by('-created')
    except Exception as e:
        print(e)
        
    page_obj = paginator.get_page(page_number)

    return render(request,'blog.html',{'page_obj':page_obj,'tags':tags,'categories':categories,'articles':articles,'articles_recent':articles_recent})

def single_blog(request,pk):
    

    article_recent = Article.objects.all().order_by('-created')[:5]
    article_populaire = Article.objects.all().order_by('-vue')[:5]
    article = Article.objects.get(pk=pk)
    article.vue = article.vue + 1
    article.save()

    try:
        
        if request.method == 'POST':
            comment = Comment.objects.create(article=article,nom_auteur=request.POST['nom'],contenu=request.POST['contenu'])
            pass
        articles = Article.objects.order_by('-created')
        articles_recent = Article.objects.order_by('-created')[:5]
        categories = Categorie.objects.all()
        tags = Tag.objects.all()
        return render(request,'single-blog.html',{'article_populaire':article_populaire,'article':article,'tags':tags,'categories':categories,'articles':articles,'article_recent':articles_recent})
        pass
    except Exception as e:
        print(e)
        #return render(request,'single-blog.html',{'article_populaire':article_populaire,'article':article,'tags':tags,'categories':categories,'articles':articles,'articles_recent':articles_recent})
        return redirect('blog')
    
    
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.POST)
        # print("SSSSSSSSSSSSSS")
        if user is not None:
            login(request, user)
            return redirect("/blog")
        # print("FAILED")

    return render(request, 'login.html')
    pass

@decorators.login_required(login_url='/login')
def modifier_blog(request,pk):
    article_recent = Article.objects.all().order_by('-created')[:5]
    article_populaire = Article.objects.all().order_by('-vue')[:5]
    categories = Categorie.objects.all()
    article = Article.objects.get(pk=pk) 
    if request.method == 'POST':
        article.titre = request.POST['titre'] 
        if request.POST['file'] != '':
            article.poster = request.FILES['file'] 
        if request.POST['categorie'] != '':
            article.categorie = Categorie.objects.get(id=request.POST['categorie'])
            
        article.contenu = request.POST['contenu']
        #article.categorie = Categorie.objects.get(id=request.POST['categorie'])
        article.save()
        return redirect(f'/single-blog/{pk}')
    
    return render(request,'modifier_blog.html',{'article_recent':article_recent,'article_populaire':article_populaire,'article':article,'categories':categories})

    pass

@decorators.login_required(login_url='/login')
def create_blog(request):
    categories = Categorie.objects.all()
    article_recent = Article.objects.all().order_by('-created')[:5]
    article_populaire = Article.objects.all().order_by('-vue')[:5]
    
    print(article_populaire,article_recent)
    if request.method == 'POST':
        try:
            #print(request.FILES)
            #print(request.POST)
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            categorie = Categorie.objects.get(id=request.POST['categorie'])
            article = Article.objects.create(poster=request.FILES['file'],titre=request.POST['titre'],contenu=request.POST['contenu'],auteur=request.user,categorie=categorie)
            #return redirect(f'/create-blog/')
        except Exception as e:
            print(e)

    return render(request,'create_blog.html',{'article_recent':article_recent,'article_populaire':article_populaire,'categories':categories})

@decorators.login_required(login_url='/login')
def create_categorie(request):
    categories = Categorie.objects.all()
    article_recent = Article.objects.all().order_by('-created')[:5]
    article_populaire = Article.objects.all().order_by('-vue')[:5]
    if request.method == 'POST':
        categorie = Categorie.objects.create(nom=request.POST['nom'])
    return render(request,'create_categorie.html',{'article_recent':article_recent,'article_populaire':article_populaire,'categories':categories})


@decorators.login_required(login_url='/login')
def modifier_categorie(request,pk):
    categories = Categorie.objects.all()
    categorie = Categorie.objects.get(pk=pk)
    article_recent = Article.objects.all().order_by('-created')[:5]
    article_populaire = Article.objects.all().order_by('-vue')[:5]
    if request.method == 'POST':
        categorie.nom = request.POST['nom']
        categorie.save()
    return render(request,'modifier_categorie.html',{'categorie':categorie,'article_recent':article_recent,'article_populaire':article_populaire,'categories':categories})


def contacter(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            objet = form.cleaned_data['objet']
            message = form.cleaned_data['message']
            datee = datetime.datetime.now().strftime("%d/%m/%Y")


            html = render_to_string('emails/contactform.html', {
                'nom': nom,
                'email': email,
                'objet': objet,
                'message': message,
                'date':datee

            })

            send_mail('the contact form subject', 'This is the message',
                      'amegahatsyondaniel@gmail.com', ['danjunio3@icloud.com'], html_message=html)
            return redirect('contacter')
    else:
        form = ContactForm()

    return render(request, 'contacter.html', {
        'form': form
    })
