from django.shortcuts import render
from django.http import HttpResponse
import random 
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length'))
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')
    uppercase = request.GET.get('uppercase')
    c='abcdefghijklmnopqrstuvwxyz'
    chars=c
    if uppercase:
        chars+=c.upper()
    if numbers: 
        chars+='0123456789'
    if special: 
        chars+='!@#%^&*()'
    password =''.join([random.choice(chars) for _ in range(length)])
    return render(request, 'generator/password.html',{'password':password})