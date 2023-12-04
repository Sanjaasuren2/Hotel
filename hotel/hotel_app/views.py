from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse
def index(request):
    return render(request, 'index.html')


def login(request):

        
    return render(request, 'login.html')

def logout(request):
    return redirect('index')



def about(request):
    return render(request, 'about.html')
def product(request):
    return render(request, 'product.html')
def room(request):
    return render(request, 'room.html')
def register(request):
 
    return render(request, 'register.html')
def uilchilgee(request):
    return render(request, 'uilchilgee.html')
