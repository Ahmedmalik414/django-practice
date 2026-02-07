from django.db import models

class Userprofile (models.Model):
    
    name= models.CharField(max_length=30)
    age= models.IntegerField()
    def __str__(self):
        return self.name

CATEGORY_CHOICES = [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
]

class Category(models.Model):
    name = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Blogpost(models.Model):  
    title= models.CharField(max_length=100) 
    content= models.TextField(max_length=1000)
    tag= models.ManyToManyField(Tag)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author= models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    

    

    

    

  
