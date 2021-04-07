from django.shortcuts import render
import requests
import json

# Create your views here.




def homepage(request):
    get = True
    data = None
    while(get):
        try:
            data = requests.get("https://api.covid19api.com/summary")
            json = data.json()
            Global = json['Global']
            Country =json['Countries']
            get = False
        except:
            get=True
            
    return render(request, "homepage.html",{'Global':Global,'Country':Country})
