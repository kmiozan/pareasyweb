from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def postList(request):
    """  """

    posts = Post.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'blog/postList.html', {'posts': posts})

def postDetail(request, pk):
    """  """

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/postDetail.html', {'post': post})

def postNew(request):
    """  """

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publishedDate = timezone.now()
            post.save()
            return redirect('postDetail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/postEdit.html', {'form': form})

def postEdit(request, pk):
    """  """

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post. author = request.user
            post.publishedDate = timezone.now()
            post.save()
            return redirect('postDetail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/postEdit.html', {'form': form})
