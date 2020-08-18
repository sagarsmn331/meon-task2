from django.db import models
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,null=True,blank=True)
    state = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        return self.name

