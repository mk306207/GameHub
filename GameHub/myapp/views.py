from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import myUser, Game, Post
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
                    return redirect("home")
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
    return render(request, 'make_post.html')

def post_maker(request):
    if request.method == "POST":
        title_input = request.POST.get("title")
        game_title_input= request.POST.get("select_game")
        gameObject = Game.objects.get(game=game_title_input)
        text_input = request.POST.get("text_input")
        user = myUser.objects.get(username = request.user.username)
        print(f"Title: {title_input}\n Game: {game_title_input}\n Text: {text_input}")
        if(game_title_input == ""):
            messages.error(request,"Please select a proper game")
            return render(request,'make_post.html')
        new_post = Post.objects.create(author=user,game_title = gameObject,title=title_input,text=text_input)
        new_post.save()
        messages.success(request,f"You have subbmited your post mr {user.get_username()}")
        return redirect("home")

def getGames(request):
    data = Game.objects.all().values('game')
    data_list = list(data)
    return JsonResponse(data_list,safe=False)

def getPosts(request):
    data = Post.objects.all().values('author','game_title','title','text')
    data_list = list(data)
    return JsonResponse(data_list,safe=False)