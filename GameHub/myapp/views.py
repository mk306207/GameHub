from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from myapp.models import usersList,userInfo

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def login_manager(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        button = request.POST.get("button")
        print(f"Login: {login_input}, Password: {password_input}")
        if button == "login":
            try:
                user = usersList.objects.get(login=login_input, password=password_input)
                request.session["user_id"] = user.id
                messages.success(request, "Succesfully logged in!")
                return redirect("dashboard")
            except usersList.DoesNotExist:
                messages.error(request, "Login or password incorrect!")
        elif button == "register":
            return redirect("register")

    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect("login")

def dashboard(request):
    if "user_id" not in request.session:
        return redirect("login")
    
    return render(request, "dashboard.html")

def register(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        email_input = request.POST.get("email")
        if login_input is None or password_input is None or email_input is None:
            messages.error(request, "Fill all the spaces!")
        print(f"Data collected:\nlogin: {login_input}\npassword: {password_input}\nemail: {email_input}")
        new_user = usersList.objects.create(login=login_input, password=password_input)
        user_email = userInfo.objects.create(logANDpsw=new_user, email=email_input)
        return redirect("login")
    return render(request, "register.html")