from django.db import models

# Create your models here.

class usersList(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.login} - {self.password}"

class userInfo(models.Model):
    logANDpsw = models.ForeignKey(usersList,on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.email