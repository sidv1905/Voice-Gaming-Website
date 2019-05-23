
from djongo import models

# Create your models here.
class Persons(models.Model):
    Username=models.CharField(max_length=255, default='No username')
    Email=models.CharField(max_length=255,default='no email')
    Password=models.CharField(max_length=255,default='no pass')
    Game =models.CharField(max_length=255,default='no game')
    Contact =models.IntegerField(default=0)
    def __str__(self):
        return self.Username


