from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    
    # nav section 
 
    #home Section
    home = Home.objects.latest('updated')
    

    #about
    about = About.objects.latest('updated')
    Profiles = Profile.objects.filter(about = about)
    
    #skills
    categories = Category.objects.all()
    
    #Profolio
    portfolios = Portfolio.objects.all()
    
    
    context = {

        'home': home,
        'about':about,
        'Profiles':Profiles,
        'categories':categories,
        'portfolios':portfolios,
        
    }
    return render(request,'index.html',context)
