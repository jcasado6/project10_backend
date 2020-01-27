from django.db import models

# Create your models here.
class Owned(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    retail_price = models.IntegerField()
    release_date = models.DateField()
    img = models.TextField()

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    retail_price = models.IntegerField()
    release_date = models.DateField()
    img = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    owns = models.ForeignKey(Owned, on_delete=models.CASCADE, related_name='owns')
    wishlist = models.ForeignKey(Wishlist, on_delete= models.CASCADE, related_name='wishlist')

    def __str__(self):
        return self.name