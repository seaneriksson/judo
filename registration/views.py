from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'registration/post_list.html', {})