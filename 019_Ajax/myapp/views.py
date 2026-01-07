from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *
import requests
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    data = request.GET['data']

    # rows = ""
    # if data=='electric':
    #     rows = "<ul><li>TV</li><li>Fan</li></ul>"
    # elif data=='sports':
    #     rows = "<ul><li>Bat</li><li>Ball</li></ul>"
    # elif data=='cosmetic':
    #     rows = "<ul><li>Facewash</li><li>lipstick</li></ul>"

    products = Product.objects.filter(name__startswith=data)
    
    return JsonResponse({"products":list(products.values())})


def add(request):

    data = requests.get("https://api.worldbank.org/v2/country?format=json").json()
    for country in data[1]:
        Country.objects.create(name=country['name'])
    return HttpResponse("done")


def countries(request):
    countries = Country.objects.all()
    return JsonResponse({"countries":list(countries.values())})

def states(request):
    cid = request.GET['cid']
    states = State.objects.filter(country_id=cid)
    return JsonResponse({"states":list(states.values())})

def cities(request):
    sid = request.GET['sid']
    cities = City.objects.filter(state_id=sid)
    return JsonResponse({"cities":list(cities.values())})