from django.db import models
from django.utils.text import slugify
import itertools
from django.contrib.auth.models import User


class Category(models.Model):
  name=models.TextField()
  def __str__(self):
     return self.name

class Media(models.Model):
    
    title = models.CharField(max_length=100,unique=True)
    content = models.TextField()
    img = models.ImageField(null=True,blank=True, upload_to='post/images')
    date = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True,max_length=500)
    categer=models.ForeignKey( Category ,on_delete=models.CASCADE )
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    is_publish=models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
      if not self.slug:
        base_slug = slugify(self.title)
        slug = base_slug
        for i in itertools.count(1):
            if not Media.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                break
            slug = f"{base_slug}-{i}"
        self.slug = slug
       
      
      super().save(*args, **kwargs)
     
    
    def __str__(self):
        return self.title

   


class About(models.Model):
    para = models.TextField(null=True)
    def __str__(self):
        return self.para


