from django.contrib import admin
from blog.models import CreateBlog

# Register your models here.
@admin.register(CreateBlog)
class BlogAdmin(admin.ModelAdmin):
  list_display=['author_name','title','content','publish_date']
  search_fields=['title']
