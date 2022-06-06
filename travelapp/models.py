from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class blog(models.Model):
    date=models.DateField()
    name1=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
    desc1=models.TextField()
    img1=models.ImageField(upload_to='picture1')





