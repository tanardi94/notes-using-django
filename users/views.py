from email import message
import imp
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration is successful.")
            return redirect("users:homepage")
        
        messages.error(request, "Registration failed due to Invalid Information")
        form = NewUserForm()
        return render(request=request, template_name="users/register.html", context={"register_form" : form})