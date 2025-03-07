from django.shortcuts import render
import requests
import datetime
def index(request):
   
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='delhi'
    API_KEY='6833cf9d769aacbf1af88dc1c37d30e3'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    PARAMS={
        'units':'metric',
    }
    data=requests.get(url,params=PARAMS)
    data=data.json()
    description=data['weather'][0]['description']
    temp=data['main']['temp']
    date_time=datetime.datetime.now()
    icon=data['weather'][0]['icon']
    return render(request,'index.html',{'description':description,'temp':temp,'date_time':date_time,'icon':icon,'city':city})

# Create your views here.
