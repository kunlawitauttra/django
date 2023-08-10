from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Kunlawit"
    age = int(40)

    return render(request,"index.html",{"name":name,"age":age})

def about(request):
    return HttpResponse("เกี่ยวกับ my first django ")
