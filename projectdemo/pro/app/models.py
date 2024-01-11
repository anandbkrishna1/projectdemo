from django.db import models
class Watch(models.Model):
    brand=models.CharField(max_length=250)
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.ImageField(upload_to='gallery')
    
    def __str__(self):
        return self.name
# Create your models here.
    # class Meta:
    #     order_with_respect_to = 'user'