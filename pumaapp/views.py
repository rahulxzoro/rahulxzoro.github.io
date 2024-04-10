from django.shortcuts import render
from . models import Shoe
# Create your views here.
def home(request):
    obj=Shoe.objects.all()

    return render(request,'index.html',{"result":obj})

def details(request,id):
    data=Shoe.objects.get(id=id)
    
    return render(request,'details.html',{"data":data})
