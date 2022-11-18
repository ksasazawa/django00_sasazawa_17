from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    img = models.TextField(null=True, blank=True)
    
class Test(models.Model):
    test_title = models.CharField(max_length=255)
    data_added = models.DateTimeField(auto_now_add=True, null=True)
    

    
# class UploadImage(models.Model):
#     image = models.ImageField(upload_to='img/')
