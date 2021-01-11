from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    msg=models.TextField()
    date=models.DateField()
    def __str__(self):
        retstr=str(self.name)+"( "+str(self.date)+" )"
        return retstr

class Info(models.Model):
    name=models.CharField(max_length=50)
    overview=models.TextField(max_length=50,default="")
    symptoms=models.TextField(max_length=50,default="")
    risk=models.TextField(max_length=50,default="")
    causes=models.TextField(max_length=50,default="")
    prev=models.TextField(max_length=50,default="")
    img=models.ImageField(default="")
    slug=models.CharField(max_length=130)
    date=models.DateField()
    def __str__(self):
        retstr=str(self.name)+"("+str(self.date)+")"
        return retstr

class News(models.Model):
    title=models.CharField(max_length=50,default="")
    content=models.TextField(max_length=100,default="")
    # link=models.TextField(default="")
    # img1= models.ImageField(default="")
    date=models.DateField()
    def __str__(self):
        retstr=str(self.title)
        return retstr


