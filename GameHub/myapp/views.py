from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from myapp.models import usersList

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def login_manager(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        print(f"Login: {login_input}, Password: {password_input}")
        try:
            user = usersList.objects.get(login=login_input, password=password_input)
            request.session["user_id"] = user.id
            messages.success(request, "Succesfully logged in!")
            return redirect("dashboard")
        except usersList.DoesNotExist:
            messages.error(request, "Login or password incorrect!")

    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect("login")

def dashboard(request):
    if "user_id" not in request.session:
        return redirect("login")
    
    return render(request, "dashboard.html")