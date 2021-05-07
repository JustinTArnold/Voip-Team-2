from django.shortcuts import render
from django.template import loader   
from django.http import HttpResponse
from django.shortcuts import redirect
import os
import csv
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def inventory(request):
    template = loader.get_template('inventory.html')
    return HttpResponse(template.render())
def save_table(request):
    info = list(request.POST.items())[0]
    info = list(info)
    info = info.pop()
    info = info.replace("\r\n","\n")
    file_path = './ucteamapp/static/assets/csv/phones.csv'
    try:
        os.remove(file_path)
    except:
        pass
    with open(file_path, 'a+') as file:
        file.write(info)

    return redirect('inventory')
