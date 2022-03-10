from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import AddPostForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        context = {
            'posts': posts
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

class BlogDetailedView(View):
    def get(self, request, pk,*args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post':post
        }
        return render(request,'view_shitpost.html', context)

class UpdateShitpost(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'update_shitpost.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:shitpost', kwargs={'pk':pk})

class DeleteShitpost(DeleteView):
    model = Post
    template_name = 'delete_shitpost.html'
    success_url = reverse_lazy('blog:home')