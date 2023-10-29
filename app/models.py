from django.db import models

# Create your models here.
class Students(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    mobile_number = models.IntegerField()
    profilepic = models.ImageField(upload_to="img",blank=True,null=True)
def __str__(self):
    return self.name
