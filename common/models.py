from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=20)
    user_second_name = models.CharField(max_length=20)
    user_age = models.IntegerField()
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=8)

    class Meta:
        db_table = 'user_tb'
        
class AdminMain(models.Model):
    admin_id = models.AutoField(primary_key=True,default="")
    admin_email = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=10)

    class Meta:
        db_table = 'admin_main'