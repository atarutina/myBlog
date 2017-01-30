from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    """
    Create a view that wll return a list of Posts that were published
    prior to 'now' and render them to the 'blogposts.html' template
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):

    post = get_object_or_404(Post, pk=id)
    post.views += 1 # clock up the numberof post views
    post.save()
    return render(request, "blogdetail.html", {'post': post})
# Create your views here.
