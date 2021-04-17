from django.db import models

class Super(models.Model):
    code_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Power(models.Model):
    ability = models.CharField(max_length=45)
    supers = models.ManyToManyField(Super, related_name="powers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)