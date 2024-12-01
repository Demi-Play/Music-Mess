from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('projects:project_list')  # Перенаправление на список проектов
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects:project_list')  # Перенаправление на список проектов
        else:
            return render(request, 'users/login.html', {'error': 'Неверные учетные данные'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')  # Перенаправление на страницу входа


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление после успешного сохранения
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'users/edit_profile.html', {'form': form})