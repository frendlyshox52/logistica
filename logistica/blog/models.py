from django.db import models

# Create your models here.

class Maxsulot(models.Model):
    name =models.CharField(max_length=100,verbose_name="title")
    image =models.ImageField(upload_to="images/",verbose_name="image")
    price =models.IntegerField(verbose_name="price")


    class Meta:
        verbose_name="maxsulot"
        verbose_name_plural="maxsulotlar"



