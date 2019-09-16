from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . models import complain

from .forms import SignUpForm
from .forms import ContactForm
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'tem/signup.html', {'form': form})

def home(request):
    return render(request,"tem/home.html")

# def contact(request):
#     if request.method=="POST":
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         msg = request.POST.get('msg', '')
#         contact = complain(name=name, email=email,msg=msg)
#         contact.save()

#     return render(request, 'tem/home.html')
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError 
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['ankushbanik123@gmail.com']) # change this to your email
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "tem/home.html", {'form': form})
 
"""You need a success view for when the form has been submitted. This will render the thank you message once the user has submitted the form. Then on the urls.py, import successView then add path('success', successView, name='success'),"""
def successView(request):
    return render(request, "tem/success.html")
        