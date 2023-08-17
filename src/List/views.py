from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_page')
def todo(request):
    
    if request.method == 'POST':
        task = request.POST.get('task')
        time = request.POST.get('time')
        
        if time is None or time == '':
            return render(request, 'index.html', {'error': 'Time cannot be empty'})
        
        if task is None or task == '':
            return render(request, 'index.html', {'error': 'Task cannot be empty'})
        
        todo = Todo.objects.create(
            task=task,
            time=time,
            )
        
        todo.save()
        
        return redirect('todo')
        
    return render(request, 'index.html', {'todos': Todo.objects.all()})

def delete_task(request, id):
     delete_task = Todo.objects.get(id=id)
     delete_task.delete()
     return redirect('todo')

def login_page(request):
    if request.method == 'POST':
        
        data = request.POST
        username = data.get('username')
        password = data.get('password')
    
        if not User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': 'User does not exist'})
        
        user = User.objects.get(username=username)
        
        if user is None:
            return render(request, 'login.html', {'error': 'User does not exist'})
        else:
            login(request, user)
            return redirect('todo')
    
    return render(request, 'login.html')

def register_page(request):
    
    if request.method == 'POST':
        
        data = request.POST
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})    
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(
            username=username,
            email=email,
            )
        
        user.set_password(password)
        user.save()
        
        messages.success(request, 'successfully registered')
        return redirect('login_page')
        
    return render(request, 'register.html')
