from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200)
    cat_description=models.TextField()

    def __str__(self):
     return self.category_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
