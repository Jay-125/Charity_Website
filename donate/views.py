from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from donate.models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import requests
import json
# Create your views here.

headers = { "X-Api-Key": "3adc9f2a0c55c49904219f78ba6dea5e", "X-Auth-Token": "a6d816b45d123db9bee68f7382d9e5db"}

def home(request):
    return render(request, 'index.html')

def Donate(request):
    if request.method == 'POST':
        n = request.POST['name']
        e = request.POST['email']
        #add = request.POST['bill']
        ph = request.POST['phone']
        amount = request.POST['amount']
        payload = {
            "purpose": "Donation Amount",
            "amount": amount,
            "buyer_name": n,
            "email": e,
            "phone":ph,
            "send_email": True,
            "send_sms":True,
            # "redirect_url": "http://127.0.0.1:8000/payment_check/"
        }
        response = requests.post("https://www.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
        print(response)
        y = response.text
        d = json.loads(y)
        print(d)
        longurl = d['payment_request']['longurl']
        return redirect(longurl)

    return render(request, 'donationform.html')