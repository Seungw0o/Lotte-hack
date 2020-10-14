from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=10)

class QR_code(models.Model):
    qr_code = models.ImageField(blank=True)
    product_name = models.CharField(max_length=20)
    product_code = models.CharField(max_length=20)
    product_image = models.ImageField(blank=True)

class Blog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    qr = models.ForeignKey(QR_code, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    receipt = models.ImageField(blank=True)
    content = models.TextField()
    approval_status = models.CharField(max_length=10)

class Admin(models.Model):
    admin_id = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=20)
    admin_level = models.IntegerField()
