from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from authentication.forms import LoginForm, SignupForm

# Create your views here.

    

# def loginPage(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password.')
#     else:
#         form = LoginForm()
#     return render(request, 'authentication/login.html',{'form': form})

def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    else:
        form = SignupForm()
    return render(request, 'authentication/signup.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    # Apply form-control class to all fields
    for field_name, field in form.fields.items():
        field.widget.attrs.update({'class': 'form-control'})
        
    return render(request, 'authentication/login.html', {'form': form})

