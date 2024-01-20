from django.shortcuts import redirect, render

from authentication.forms import SignupForm

# Create your views here.
def loginPage(request):

    return render(request, 'authentication/login.html')


def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'authentication/signup.html', {'form': form})
