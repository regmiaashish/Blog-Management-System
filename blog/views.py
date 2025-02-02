from django.shortcuts import render,redirect
from blog.forms import BlogForm
from blog.models import CreateBlog

# Create your views here.

def info_blog(request):
  content={"data":"Welcome to the Blog page"}
  return render(request,'blogs/home.html',content)


def create_blog(request):
  form=BlogForm()
  if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-blog")
        else:
            return form.errors

  info = {"data": "Form FillUp", "form": form}
  return render(request, "blogs/create.html", info)


def list_Blog(request):
    context = {"data": CreateBlog.objects.all()}
    return render(request, "blogs/list.html", context)



def edit_blog(request, id):
    broadway_blog = CreateBlog.objects.get(id=id)
    form = BlogForm(instance=broadway_blog)
    if request.method == "POST":
        form = BlogForm(
            request.POST, request.FILES or None, instance=broadway_blog
        )
        if form.is_valid():
            form.save()
            return redirect("list-blog")
        else:
            return form.errors
   
    context = {"data": broadway_blog, "form": form}
    return render(request, "blogs/edit.html", context)


def delete_blog(request,id):
    CreateBlog.objects.get(id=id).delete()
    return redirect("list-blog")



def view_blog(request, id):
    content = CreateBlog.objects.filter(id=id)
    context = {"data": content}
    return render(request, "blogs/view.html", context)


    
    
  