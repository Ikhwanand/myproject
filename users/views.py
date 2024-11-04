from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { "form": form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('posts:list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form' : form })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    
    return render(request, 'users/logout.html')
