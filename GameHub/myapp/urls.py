from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login_view",views.login_manager,name="login_view"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("logout_handler", views.logout_handler, name="logout_handler"),
    path("register",views.register,name="register"),
    path("delete_user", views.delete_user, name = "delete_user"),
    path("make_post",views.make_post,name="make_post"),
    path("post_maker",views.post_maker,name="post_maker"),
    path("api/getGames",views.getGames,name="getGames"),
    path("api/getPosts",views.getPosts,name="getPosts"),
    path('like_post/', views.likePost, name='like_post'),
    path('view_profile/<int:user_id>',views.view_profile,name="view_profile"),
    path('api/checkLike',views.checkLike,name="checkLike"),
    path("link_account",views.link_account,name="link_account"),
    path("create_linkedAcc",views.create_linkedAcc,name="create_linkedAcc"),
    path('api/returnMyAccounts',views.returnMyAccounts,name="returnMyAccounts"),
    path('view_profile/api/returnMyAccounts',views.returnMyAccounts,name="returnMyAccounts"),
    path('PMs', views.PMs,name="PMs"),
]
