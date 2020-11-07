from django.shortcuts import render
from .models import Contact
import datetime

def index(request):
    return render(request, 'website/index.html')

def contact_form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        telegram = request.POST['telegram']
        message = request.POST['message']
        contact = Contact(name=name, email=email, telegram=telegram, message=message, date=datetime)
        contact.save()

        return render(request, 'website/thankyou.html')
    else:
        return render(request, 'website/index.html')