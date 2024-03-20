from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("hello")

def hfirst(request):
    return render(request,'index.html')