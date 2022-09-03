from pickletools import read_uint1
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'cp/home.html')

def s_signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = User.objects.last()
            name = request.POST.get('name')
            email = request.POST.get('email')
            hostel = request.POST.get('hostel')
            room_no = request.POST.get('room_no')
            roll_no = request.POST.get('username')
            
            print(user,name,email,hostel,room_no,roll_no)
            Student.objects.create(
                user = user,
                name = name,
                email = email,
                roll_no = roll_no,
                hostel = hostel,
                room_no = room_no
            )

            return redirect('s_login')

    return render(request, 'cp/s_signup.html')

def s_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        login(request,user)

        return redirect('portal')
    return render(request, 'cp/s_login.html')

def portal(request):
    return render(request, 'cp/portal.html')