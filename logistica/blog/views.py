from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
#
# def home(request):
#     return render(request, 'index.html')


from django.shortcuts import render

def home(request):
    return render(request, 'blog/index.html')