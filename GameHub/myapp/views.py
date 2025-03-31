from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import myUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def login_manager(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        button = request.POST.get("button")
        print(f"Login: {login_input}, Password: {password_input}")
        if button == "login":
            try:
                user = myUser.objects.get(username = login_input)
                #print(f"correct username: {user.get_username()} correct password: {user.password} {user.check_password(password_input)}")
                if user.check_password(password_input):
                    messages.success(request, "Welcome back!")
                    login(request,user)
                    return redirect("dashboard")
                else:
                    messages.error(request,"Wrong password!")
            except ObjectDoesNotExist:
                messages.error(request, "Wrong username!")
            # if():
            #     return redirect("dashboard")
        elif button == "register":
            return redirect("register")

    return render(request, "login.html")

def logout_handler(request):
    logout(request)
    return redirect("login_view")

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login_view")
    return render(request, "dashboard.html")

def register(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        email_input = request.POST.get("email")
        if login_input is None or password_input is None or email_input is None:
            messages.error(request, "Fill all the spaces!")
            return render(request, "register.html")
        print(f"Data collected:\nlogin: {login_input}\npassword: {password_input}\nemail: {email_input}")
        new_user = myUser.objects.create(username=login_input,email=email_input)
        new_user.set_password(password_input)
        new_user.save()
        return redirect("login_view")
    return render(request, "register.html")

def delete_user(request):
    user = myUser.objects.get(username = request.user.username)
    logout(request)
    user.delete()
    messages.error(request, "User deleted")
    return redirect("login_view")

def make_post(request):
    user = myUser.objects.get(username = request.user.username) #TODO
    return redirect(request, 'post_text_field')             #TODO