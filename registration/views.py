from django.shortcuts import render
from .forms import PostForm


# Create your views here.
def post_list(request):
    return render(request, 'registration/post_list.html', {})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'registration/post_edit.html', {'form': form})
            ##print success 
    else:
        form = PostForm()
    return render(request, 'registration/post_edit.html', {'form': form})