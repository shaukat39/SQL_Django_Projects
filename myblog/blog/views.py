# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Redirect to the blog list after saving
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_blog_post.html', {'form': form})

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})


