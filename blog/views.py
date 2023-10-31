from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        ## DESDE AQUÍ SE LLAMA LOS DATOS EN LA BB.DD. con objects.all()
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'blog_list.html', context)
    


class BlogCreateView(View):

    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form':form
        }
        return render(request, 'blog_create.html',context)
    

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')


            post, created = Post.objects.get_or_create(title=title, content=content)
            post.save()
            return redirect('blog:Home')

        context = {
            
        }
        return render(request, 'blog_create.html',context)
        

class BlogDetailView(View):
    def get (self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post':post
        }

        return render(request, 'blog_detail.html', context)
