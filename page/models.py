from django.db import models

# Create your models here.
class Car(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()


class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)