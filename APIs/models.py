from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Bedaia(models.Model):
    title = models.CharField(max_length=200)
    firstdiscription = models.TextField()
    seconddiscription = models.TextField()
    slug = models.SlugField(max_length=255, null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at =models.DateTimeField(auto_now=True)
    firstpic =  models.ImageField(upload_to='images/',blank=True)
    secondpic =  models.ImageField(upload_to='images/',blank=True)
    thirdpic =  models.ImageField(upload_to='images/',blank=True)
    forthpic =  models.ImageField(upload_to='images/',blank=True)
    video_file = models.FileField(upload_to='videos/',blank=True)
    upload_file = models.FileField(upload_to='upload_folder/',blank=True)
    
    class Meta:
        ordering=['-created_at']
    
    def __str__(self):
        return self.title
    def save(self ,*args ,**kwargs):
        to_assign=slugify(self.title)

        if Bedaia.objects.filter(slug=to_assign).exists():
            to_assign=to_assign+str(Bedaia.objects.all().count())
        
        self.slug=to_assign
        
        super().save(*args, **kwargs)

class Nukhba(models.Model):
    title = models.CharField(max_length=200)
    firstdiscription = models.TextField()
    seconddiscription = models.TextField()
    slug = models.SlugField(max_length=255, null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at =models.DateTimeField(auto_now=True)
    firstpic =  models.ImageField(upload_to='images/',blank=True)
    secondpic =  models.ImageField(upload_to='images/',blank=True)
    thirdpic =  models.ImageField(upload_to='images/',blank=True)
    forthpic =  models.ImageField(upload_to='images/',blank=True)
    video_file = models.FileField(upload_to='videos/',blank=True)
    upload_file = models.FileField(upload_to='upload_folder/',blank=True)
    class Meta:
        ordering=['-created_at']
    
    def __str__(self):
        return self.title
    def save(self ,*args ,**kwargs):
        to_assign=slugify(self.title)

        if Nukhba.objects.filter(slug=to_assign).exists():
            to_assign=to_assign+str(Nukhba.objects.all().count())
        
        self.slug=to_assign
        
        super().save(*args, **kwargs)

