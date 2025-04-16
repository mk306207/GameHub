from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import myUser, Game, Post, postRatings, myCustonDict
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json, sys

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
    return render(request, 'make_post.html',{'m':"makePost"})

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
    
def link_account(request):
    return render(request,"make_post.html",{'m':'linkAccount'})
    
def create_linkedAcc(request):
    if request.method == "POST":
        game_input = request.POST.get("select_game")
        nickname_input = request.POST.get("nickname")
        gameObject = Game.objects.get(game=game_input)
        print(f"game: {game_input}, nickname: {nickname_input}")
        gameAccount = myCustonDict.objects.filter(nickname = nickname_input, game = gameObject)
        if gameAccount:
            gameAccount = myCustonDict.objects.get(nickname = nickname_input)
            messages.error(request,f"This account is already linked to account called \"{gameAccount.user_id.username}\"")
        else:
            gameAccount = myCustonDict.objects.create(user_id = request.user, nickname = nickname_input, game = gameObject)
            gameAccount.save()
            messages.success(request,"Linked!")
        return redirect("dashboard")

def getGames(request):
    data = Game.objects.all().values('game')
    data_list = list(data)
    return JsonResponse(data_list,safe=False)

def getPosts(request):
    data = Post.objects.all().values('id','author','game_title','title','text','score')
    data_list = list(data)
    for i in range(0,len(data_list)):
        data_list[i]['authorID'] = getAuthorObject(data_list[i]['author'])
    #print(data_list)
    return JsonResponse(data_list,safe=False)

def likePost(request):
    if request.method=="POST":
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id = post_id)
        liked = postRatings.objects.filter(post_id = post, user_id = request.user)
        liked_flag = False
        if not liked:
            liked = postRatings.objects.create(post_id = post, user_id = request.user)
            post.score = post.score + 1
            print("+1")
            liked_flag=True
            post.save()
        else:
            liked = postRatings.objects.filter(post_id = post, user_id = request.user).delete()
            post.score = post.score-1
            print("-1")
            post.save()
            liked_flag=False
        return JsonResponse({'message': 'Success!', 'new_score':post.score, 'liked_flag':liked_flag})
    return JsonResponse({'error':'error_400',},status=400)

def view_profile(request,user_id):
    author = myUser.objects.get(id = user_id)
    if author == request.user:
        return render(request,"dashboard.html")
    if author:
        return render(request,"view_profile.html",{'author':author})
    else:
        messages.error("Invalid user id")
    
def checkLike(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id = post_id)
        try:
            post_liked = postRatings.objects.get(post_id = post,user_id = request.user)
            if post_liked:
                flag = True
                return JsonResponse({'message':'success', 'flag':flag})
        except ObjectDoesNotExist:
                flag = False
                return JsonResponse({'message':'success','flag':flag})
    return JsonResponse({'error':'error_400',},status=400)

def getAuthorObject(data):
    try:
        user = myUser.objects.get(username=data)
        #print(user.id)
        return user.id
    except ObjectDoesNotExist:
        print("We do not expect that!")
        return 0
    
def returnMyAccounts(request):
    if request.method == 'POST':
        switch = request.POST.get('switch');print(switch)
        if switch == "self":
            data = list(myCustonDict.objects.filter(user_id = request.user).values('user_id','nickname','game'))
            return JsonResponse(data,safe=False)
        elif switch == "other":
            authorID = request.POST.get('authorID')
            data = list(myCustonDict.objects.filter(user_id = authorID).values('user_id','nickname','game'))
            return JsonResponse(data,safe=False)
    else:
        print("Doesnt work...")
    