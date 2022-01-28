from distutils.log import error
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import *
from .forms import UserCreationForm, CreateUserForm

# Create your views here.


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')

            print(username, password)

            messages.success(
                request, 'Account Succesfully Created for ' + username)

            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'app/register.html', context)


def loginUser(request,):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password is INCORRCT!')

    return render(request, 'app/login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def addItem(request):
    user = request.user

    current_date = timezone.now()
    heading = request.POST['content']
    description = request.POST['description']
    new_item = todo(date_created=current_date,
                    content=heading, author=user, description=description)
    new_item.save()

    print(user.id)
    return HttpResponseRedirect('/')


@login_required(login_url='login')
def home(request,):
    user = request.user
    todoItem = todo.objects.filter(author=user.id).order_by("-date_created")

    # users_items = user.todo_set.filter(author=user.id)

    context = {
        'todoItems': todoItem,

    }
    return render(request, 'app/main.html', context)


@login_required(login_url='login')
def deleteItem(request, pk):
    if request.method == 'POST':
        item = todo.objects.get(id=pk)
        item.delete()

    return HttpResponseRedirect('/')
