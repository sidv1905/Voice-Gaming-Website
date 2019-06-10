from django.shortcuts import render,HttpResponse
from .models import Persons
# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')
def login(request):
    if request.method=="POST":
        Username=request.POST.get('name')
        Password=request.POST.get('password')
        q1 = Persons.objects.filter(Username=Username,Password=Password).first()
        print(q1)
        if q1 is not None:
            request.session['loggedin']=True
            return render(request,'mainapp/home.html' ,{'person': q1})
    return render(request,'mainapp/login.html')
def registration(request):
    if request.method=='POST':
        #'NAME , EMAIL, PASSWORD, CONTACT, GAME CHOICE,;
        name=request.POST.get('name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        game=request.POST.get('game')
        contact=request.POST.get('contact')
        person=Persons()
        person.Username=name
        person.Password=password
        person.Email=email
        person.Contact=contact
        person.Game=game
        person.save()
        return render(request,'mainapp/login.html')

    return render(request,'mainapp/registration.html')
def logout(request):
   try:
      del request.session['loggedin']
   except:
      pass
   return render(request, 'mainapp/logout.html')

def game(request):
    return render(request,'mainapp/Game.html')
def ladder(request):
    return render(request,'mainapp/snakeladder.html')