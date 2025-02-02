from django.urls import path
from blog.views import info_blog, create_blog, list_Blog, edit_blog, delete_blog, view_blog

urlpatterns = [
    path('', info_blog, name="information"),
    path('form/', create_blog, name="create-blog"),
    path('list/', list_Blog, name="list-blog"),
    path('edit/<int:id>/', edit_blog, name="edit-blog"),
    path('delete/<int:id>/', delete_blog, name="delete-blog"),
    path('view/<int:id>/', view_blog, name="view-blog"),
]
