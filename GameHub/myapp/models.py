from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class usersList(models.Model):
#     login = models.CharField(max_length=25)
#     password = models.CharField(max_length=100)
    
#     def __str__(self):
#         return f"{self.login} - {self.password}"

# class userInfo(models.Model):
#     logANDpsw = models.ForeignKey(usersList,on_delete=models.CASCADE)
#     email = models.EmailField()
    
#     def __str__(self):
#         return self.email

class myUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    def save(self, *args, **kwargs):
        self.first_name = ""
        self.last_name = ""
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.id)
    def get_password(self):
        return self.password
    
class Game(models.Model):
    game = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.game

class myCustonDict(models.Model):
    user_id = models.ForeignKey(myUser,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    
class Post(models.Model):
    author = models.ForeignKey(myUser,on_delete=models.CASCADE, to_field="username")
    game_title = models.ForeignKey(Game, on_delete=models.DO_NOTHING, to_field="game",null=False,blank=False)
    title = models.CharField(max_length=50)
    text = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Author: {self.author}\nGame title: {self.game_title}\nTitle: {self.title}\nText:{self.text}\n"

class postRatings(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE,to_field="id")
    user_id = models.ForeignKey(myUser,on_delete=models.CASCADE,to_field="id")