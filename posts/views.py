from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    #If the method is POST
    if request.method == 'POST':
        form= PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid(): 
            #Yes, Save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')
        else:
            #No, Error
            return HttpResponseRedirect(form.errors.as_json())
   
    #get all post
    posts= Post.objects.all().order_by('-created_at')[:20]
     

    #show
    return render( request , 'posts.html',
                    {'posts': posts})
                    
    
def delete(request, post_id):
    post=Post.objects.get(id = post_id)
    post.delete()
    #output= 'POST ID is ' + str(post_id)
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST' :
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")

    form =PostForm

    return render(request, 'edit.html', {'post':post, 'form':form})



def LikeView(request, post_id):
    new_value = Post.objects.get(id=post_id)
    new_value.likes +=1
    new_value.save()
    return HttpResponseRedirect('/')
    