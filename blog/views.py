from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import AddPostForm
from .models import Post

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = AddPostForm()

        context = {
            'form':form
        }
        return render(request,'add_post.html', context)

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')

        context = {

        }
        return render(request, 'add_post.html', context)

