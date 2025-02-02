from django import forms
from blog.models import CreateBlog

class BlogForm(forms.ModelForm):
  class Meta:
    model=CreateBlog
    exclude=['publish_date']