from django.db import models

# Create your models here.
class MovieModel(models.Model):
    mname=models.CharField(max_length=30)
    director=models.CharField(max_length=15)
    rating=models.FloatField()
    genre=models.CharField(max_length=15)
    price=models.FloatField()
    release_date=models.DateTimeField(auto_now_add=True)
    avail=models.BooleanField()
    
    def __str__(self):
        return self.mname
    
class UsersModel(models.Model):
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    email=models.EmailField()
    addr=models.CharField(max_length=15)
        
    def __str__(self):
        return self.name

class Booking(models.Model):
    users=models.ForeignKey(UsersModel,on_delete=models.CASCADE)
    movies=models.ForeignKey(MovieModel,on_delete=models.CASCADE)
    mov_date=models.DateField()
    tickets=models.IntegerField()
    tot_price=models.FloatField(blank=True,null=True)