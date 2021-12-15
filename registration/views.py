from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import *
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = Createuserform
        if request.method == "POST":
            form = Createuserform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account is created")
                return redirect('/login')
        context = {
            'form':form
        }
        return render(request, 'registration/signup.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "username or password is incorrect")
    return render(request,'registration/login.html',)


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/login')