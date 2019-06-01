from django.shortcuts import render, redirect
from .forms import PostForm, LoginForm,commentForm
from .models import Comments, Post

# Create your views here.
def home_page(request):
	post = Post.objects.order_by('-id') 
	return render(request, "index.html", {'post':post})
	
	


def new_post(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.save()
		return redirect('/home')
	return render(request, "post.html", {'form':form})
	


def category(request):
	return render(request, "category.html", {})
	post = Post.objects.order_by('-id')	


def login(request):
	form = LoginForm()

	if request.method == 'POST':
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				login(request, user)
				return redirect('/home')
			#if user:
	return render(request, 'login.html', {'form':form})