from django.shortcuts import render
import razorpay
from django.http import HttpResponse,JsonResponse 
from django.core.mail import send_mail
from django.conf import settings
import requests
# Create your views here.
def index(request):
    return render(request,"index.html")


def payment(request):
    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    print(payment)
    return JsonResponse(payment)


def sendmail(request):
    try :
        send_mail("Testing","testing",settings.EMAIL_HOST_USER,["chintan.tops@gmail.com"],html_message="<h1>Hello</h1>")
        print("email sent successsfully")
    except Exception as e:
        print(e)


def sendsms(request):
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"APIKEY","message":"This is test message","language":"english","route":"q","numbers":"9106950290"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


