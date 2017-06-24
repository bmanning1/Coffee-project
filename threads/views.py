from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import ThreadForm, PostForm
from threads.models import Subject, Post, Thread
from django.forms import formset_factory
from polls.forms import PollSubjectForm, PollForm
from polls.models import PollSubject
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Forum views:
# Search Subjects, List Subjects, List Threads, Singular Thread, New Thread,
# New Post, Edit Post, Delete Post and Thread Vote

def results(request):
    """ Subject search ('forum/search.html' template) """
    q = request.GET.get('q')
    threads = Thread.objects.filter(subject__name=q)
    return render(request, 'forum/search.html', {'threads': threads})


def forum(request):
    """ List Subjects view with paginator wrapping at 6 Subjects ('forum/forum.html' template) """
    page = request.GET.get('page', 1)
    all_subjects = Subject.objects.all()
    subject = Subject.objects.all().order_by('-id')
    paginator = Paginator(subject, 6)
    try:
        subjects = paginator.page(page)
    except PageNotAnInteger:
        subjects = paginator.page(1)
    except EmptyPage:
        subjects = paginator.page(paginator.num_pages)
    return render(request, 'forum/forum.html', {'subjects': subjects, 'all_subjects': all_subjects})


def threads(request, subject_id):
    """ List Threads for a Subject with paginator wrapping at 4 Threads ('forum/threads.html' template) """
    subject = get_object_or_404(Subject, pk=subject_id)
    subject_threads0 = subject.threads.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(subject_threads0, 4)
    try:
        subject_threads = paginator.page(page)
    except PageNotAnInteger:
        subject_threads = paginator.page(1)
    except EmptyPage:
        subject_threads = paginator.page(paginator.num_pages)
    return render(request, 'forum/threads.html', {'subject': subject, 'subject_threads': subject_threads})


def thread(request, thread_id):
    """ Singular Thread view with paginator wrapping at 4 Posts ('forum/thread.html' template) """
    thread_ = get_object_or_404(Thread, pk=thread_id)
    thread_posts0 = thread_.posts.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(thread_posts0, 4)
    try:
        thread_posts = paginator.page(page)
    except PageNotAnInteger:
        thread_posts = paginator.page(1)
    except EmptyPage:
        thread_posts = paginator.page(paginator.num_pages)
    args = {'thread': thread_, 'thread_posts': thread_posts}
    args.update(csrf(request))
    return render(request, 'forum/thread.html', args)


@login_required
def new_thread(request, subject_id):
    """ Create a new Thread view and Poll with 3 options with login required('forum/thread_form.html' template) """
    subject = get_object_or_404(Subject, pk=subject_id)
    poll_subject_formset = formset_factory(PollSubjectForm, extra=3)
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        poll_form = PollForm(request.POST)
        poll_subject_formset = poll_subject_formset(request.POST)
        if thread_form.is_valid() and post_form.is_valid() and poll_form.is_valid() and poll_subject_formset.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()

            poll = poll_form.save(False)
            poll.thread = thread
            poll.save()

            for subject_form in poll_subject_formset:
                subject = subject_form.save(False)
                subject.poll = poll
                subject.save()

            messages.success(request, "You have created a new thread!")

            return redirect(reverse('thread', args={thread.pk}))

    else:
        thread_form = ThreadForm()
        post_form = PostForm(request.POST)
        poll_form = PollForm()
        poll_subject_formset = poll_subject_formset()

    args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
        'poll_form': poll_form,
        'poll_subject_formset': poll_subject_formset,
    }

    args.update(csrf(request))

    return render(request, 'forum/thread_form.html', args)


@login_required
def new_post(request, thread_id):
    """ New Post view with login required ('forum/post_form.html' template) """
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request, "Your post has been added to the thread!")

            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm()

    args = {
        'form': form,
        'form_action': reverse('new_post', args={thread.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))

    return render(request, 'forum/post_form.html', args)


@login_required
def edit_post(request, thread_id, post_id):
    """ Edit post view with login required ('forum/post_form.html' template) """
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "You have updated your thread!")

            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'form_action': reverse('edit_post', kwargs={"thread_id": thread.id, "post_id": post.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))

    return render(request, 'forum/post_form.html', args)


@login_required
def delete_post(request, thread_id, post_id):
    """ Delete Post view with login required """
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    messages.success(request, "Your post was deleted!")

    return redirect(reverse('thread', args={thread_id}))


@login_required
def thread_vote(request, thread_id, subject_id):
    """ Thread vote view with login required """
    thread = Thread.objects.get(id=thread_id)

    subject = thread.poll.votes.filter(user=request.user)

    if subject:
        messages.error(request, "You've already voted on this... You're not trying to cheat, are you?!")
        return redirect(reverse('thread', args={thread_id}))

    subject = PollSubject.objects.get(id=subject_id)

    subject.votes.create(poll=subject.poll, user=request.user)

    messages.success(request, "We've registered your vote!")

    return redirect(reverse('thread', args={thread_id}))
