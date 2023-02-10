from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    number = models.IntegerField(default=0)
    number1 = models.IntegerField(default=1)
    slug = models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.name