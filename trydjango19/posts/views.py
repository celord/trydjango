from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .form import PostForm
from .models import Post


# Create your views here.


def posts_create(request):
    
    form = PostForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, "Succsessfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Succesfully created")
        context = {
            "form":form,
        }
    return render(request, "post_form.html", context)

def posts_detail(request,id=None):
    
    #Post.objects.get(id=18)
    instance = get_object_or_404(Post,id=id)    
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
    
    return render(request, "post_list.html",context)

def posts_update(request, id=None):
    
    #Post.objects.get(id=18)
    instance = get_object_or_404(Post,id=id) 

    form = PostForm(request.POST or None, instance=instance)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title" : instance.title,
        "instance" : instance,
        "form":form,
        }
    return render(request, "post_form.html", context)

def posts_delete(request, id=None):
    
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, "Succsessfully Deleted")
    return redirect("posts:list")