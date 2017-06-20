from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Blog views: Search, List of Blog posts, Singular Blog post and Edit a Blog post

def blogresults(request):
    # Subject search ('blog/blogsearch.html' template)
    q = request.GET.get('q')
    posts = Post.objects.filter(title=q)
    return render(request, 'blog/blogsearch.html',{'posts':posts})

def post_list(request):
    # List of Blog posts published prior to 'now' view ('blogposts.html' template)
    all_posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    # Create a Paginator that wraps at 4 posts
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, "blog/blogposts.html", {'posts': blogs, 'all_posts': all_posts})


def post_detail(request, id):
    # Single Blog post view based on post ID ('postdetail.html' template), or return a 404 error if no post found
    post = get_object_or_404(Post, pk=id)
    # Add up the number of post views
    post.views += 1
    post.save()
    return render(request, "blog/postdetail.html", {'post': post})


def edit_post(request, id):
    # Edit the Blog post view ('blogpostform.html template)
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
