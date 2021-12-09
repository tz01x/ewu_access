from django.shortcuts import render

# Create your views here.

def indexview(req):
    return render(req,'core/index.html')