from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def postList(request):
    """  """

    posts = Post.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'blog/postList.html', {'posts': posts})

def postDetail(request, pk):
    """  """

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/postDetail.html', {'post': post})
