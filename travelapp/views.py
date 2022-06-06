from django.shortcuts import render
from . models import place
from . models import blog

def fun(request):
    obj=place.objects.all()
    obj1=blog.objects.all()
    context={'results':obj,'blogresults':obj1}
    return render(request,"index.html",context)


def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})

