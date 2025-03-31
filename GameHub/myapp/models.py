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
    email = models.EmailField(unique=True)
    def save(self, *args, **kwargs):
        self.first_name = ""
        self.last_name = ""
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username
    def get_password(self):
        return self.password
    
class Post(models.Model):
    author = models.ForeignKey(myUser,on_delete=models.CASCADE, to_field="username")
    text = models.TextField()