from django.shortcuts import render,redirect,get_object_or_404
from .form import PostForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import Post

def delete(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post.delete()
    return redirect("/post")

def like(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post.like += 1
    post.save()
    return redirect("/post")


def dislike(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post.dislike += 1
    post.save()
    return redirect("/post")

@csrf_exempt 
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("form is not valid")
    form = PostForm()
    data = Post.objects.all()
    return render(request,"post/index.html",context={'form':form,'data':data})

# Create your views here.
