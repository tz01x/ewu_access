from django.shortcuts import render

# Create your views here.

from .forms import MyUserCreationForm
def signup(req):

    form=MyUserCreationForm()

    contex={
        'form':form
    }
    return render(req,'user/signup.html',contex)