from django.http import  HttpResponse
from django.shortcuts import render, get_object_or_404
from .form import PostForm

from .models import Post


# Create your views here.


def posts_create(request):
    
    
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        

    context = {
        "form":form,
        }
    return render(request, "post_form.html", context)

def posts_detail(request,idd):
    
    #Post.objects.get(id=18)
    instance = get_object_or_404(Post,id=idd)    
    context = {
        "title" : instance.title,
        "instance" : instance,
        }
    return render(request, "post_detail.html", context)

def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title":"List",
        }
    
    return render(request, "index.html",context)

def posts_update(request):
    
    return HttpResponse("<h1>Update</h1>")

def posts_delete(request):
    
    return HttpResponse("<h1>Delete</h1>")