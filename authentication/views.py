from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request, 'authentication/login.html')


def signupPage(request):
    return render(request, 'authentication/signup.html')
