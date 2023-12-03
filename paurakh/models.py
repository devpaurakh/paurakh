from django.db import models

# Create your models here.

#This model for the home page

    
class Home(models.Model):
    fullName= models.CharField(max_length=20)
    greetingOne = models.CharField(max_length=5)
    greetingTwo = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='photos/') 
    
    #It will modified when it saved
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return self.fullName
   
   # about page of my self
class About(models.Model):
    title = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    photo = models.ImageField(upload_to='photos/')
     #It will modified when it saved
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.position
    
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    socialMedia = models.CharField(max_length=10)
    link = models.URLField(max_length=200)
    
#skill portion
class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    def __str__(self):
        return f'Portfolio{self.id}'