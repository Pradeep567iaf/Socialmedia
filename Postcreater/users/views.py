from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print("welcome to the registration form ")
        if form.is_valid():
            form.save()
            print("registered successfully")
            return redirect('login')
    else:
        form = UserRegistrationForm()
        print("Invalid entry", request.POST)
    return render(request,'register.html',{'form':form}) 

def profile(request):
    print(request.user)
    return render(request,'profile.html',{})




