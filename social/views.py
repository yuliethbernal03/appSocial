from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import Post_form, Register_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def feed_view(request):
    posts = Post.objects.all()

    context = { 'posts': posts}
    return render(request, 'feed.html', context)

def register_view(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado.')
            return redirect('/')
    else: 
        form = Register_form()

    context = { 'form': form }
    return render(request, 'register.html', context)

def profile_view(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else: 
        posts = current_user.posts.all()
        user = current_user

    return render(request, 'profile.html', {'user': user, 'posts': posts})

@login_required
def post_view(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.user =current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect ('/')
    else:
        form = Post_form()
    return render(request, 'post.html', {'form' : form})

def follow_view(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Sigues a {username}')
    return redirect('/')

def unfollow_view(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Dejaste de seguir a {username}')
    return redirect('/')
    