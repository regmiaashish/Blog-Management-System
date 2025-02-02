from django.db import models

# Create your models here.

class CreateBlog(models.Model):
  author_name=models.CharField(max_length=200,null=False)
  title=models.CharField(max_length=255,null=False)
  content=models.TextField(null=False)
  publish_date=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.title}-{self.author_name}"




