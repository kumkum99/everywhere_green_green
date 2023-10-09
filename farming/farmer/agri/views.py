from django.core.checks import messages
import email
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.core.mail import send_mail
from django.urls import reverse

from .models import ContactForm
from .models import ApprenticeShip


# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


def ourproduct(request):
    template = loader.get_template('ourproduct.html')
    return HttpResponse(template.render())


def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())


def weather(request):
    template = loader.get_template('weather.html')
    return HttpResponse(template.render())


def farming(request):
    template = loader.get_template('farming.html')
    return HttpResponse(template.render())


def bestfarmers(request):
    template = loader.get_template('bestfarmers.html')
    return HttpResponse(template.render())


def signup(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']

        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            error_message = "Username already exists. Please choose a different username."
            return render(request, 'signup.html', {'error_message': error_message})

        # Create the new user
        new_user = User.objects.create_user(username=uname, email=email, password=pass1)

        # Handle successful user creation, such as redirecting to a success page or login page
        return HttpResponseRedirect('login')  # Replace 'login' with the actual name of your login view

    # Handle GET request or successful user creation
    return render(request, 'signup.html')


def auth_login(request, user):
    pass


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Change 'pass' to 'password'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login to log the user in
            return redirect('home')  # Replace 'home' with the actual URL name for your home page
        else:
            # Display an error message on the login page
            error_message = 'Username and password are incorrect!!'
            # You can also log the failed login attempt if needed
            # Log the error message, or use Django's built-in logging framework

            # Sending an email for a failed login attempt (Not recommended)
            send_mail(
                "Failed Login Attempt",
                f"Failed login attempt for username: {username}",
                "agrovillage2024@gmail.com",
                [email],
                fail_silently=False,
            )

            # Pass the error message to the template for display
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('home')


def index_view(request):
    # Your view logic here
    return render(request, 'index.html')


def home_view(request):
    # Your view logic here
    return render(request, 'home.html')


def about_view(request):
    # Your view logic here
    return render(request, 'about.html')


def news_view(request):
    # Your view logic here
    return render(request, 'news.html')


def contact_view(request):
    # Your view logic here
    return render(request, 'contact.html')


def shop_views(request):
    return render(request, 'shop.html')


def ourproduct_views(request):
    return render(request, 'ourproduct.html')


def newsd_views(request):
    return render(request, 'newsd.html')


def farming_views(request):
    return render(request, 'farming.html')


def weather_views(request):
    return render(request, 'weather.html')


def login_views(request):
    return render(request, 'login.html')


def bestfarmers_views(request):
    return render(request, 'bestfarmers.html')


def saveEnquiry(request):
    show_alert = False  # Initialize to False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        en = ContactForm(name=name, email=email, subject=subject, message=message)
        en.save()
        show_alert = True  # Set to True after form submission
    return render(request, 'contact.html', {'show_alert': show_alert})


def cart_page(request):
    return render(request, 'cart.html')


def pay(request):
    return render(request, 'payment.html')


def aprenticeship(request):
    show_alert = False  # Initialize to False
    if request.method == 'POST':
        fname = request.POST.get('name')
        mail = request.POST.get('email')
        subj = request.POST.get('subject')
        mess = request.POST.get('message')
        fn = ApprenticeShip(name=fname, email=mail, subject=subj, message=mess)
        fn.save()
        show_alert = True  # Set to True after form submission
    return render(request, 'farming.html', {'show_alert': show_alert})


def confirmation(request):
    return render(request, 'passreser_confirm.html')
