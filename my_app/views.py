from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import datetime
from django.utils import timezone
from django.views import generic




def post_list(request): 
	posts = Post.objects.order_by('created_date')
	return render(request, 'my_app/post_list.html',
		{'posts': posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now() 
			post.save() 
			return redirect('post_list') 
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html',
{'form': form}) 

