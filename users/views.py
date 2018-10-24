from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You have successfully created an account. you can login now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
