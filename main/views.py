from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import ReportForm
from .models import Report
from django import forms


# Create your views here.
def homepage(request):
    return render(request, 'main/home.html')


def centralfaultpage(request):
    return render(request, 'main/central_faults.html')


def northfaultpage(request):
    return render(request, 'main/north_faults.html')


def southfaultpage(request):
    return render(request, 'main/south_faults.html')


def registerpage(request):
    if request.method == 'GET':
        return render(request, 'main/register.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)

            login(request, user)
            return redirect('home')
        else:
            return redirect('register')


def loginpage(request):
    if request.method == 'GET':
        return render(request, 'main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'user is invalid')
            return redirect('login')


def logoutpage(request):
    logout(request)
    return redirect('login')


def escomcentralpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escom-central')
        
    report_count = reports.count()

    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/escom/escom_central.html', context)


def deletepage(request):
    reports = Report.objects.all()
    if request.method == 'POST':
        reports.delete()
        return redirect('escom-central')
    return render(request, 'main/delete.html')


def escomnorthpage(request):
    return render(request, 'main/escom/escom_north.html')


def escomsouthpage(request):
    return render(request, 'main/escom/escom_south.html')


def constructioncentralpage(request):
    return render(request, 'main/construction/construction_central.html')


def constructionnorthpage(request):
    return render(request, 'main/construction/construction_north.html')


def constructionsouthpage(request):
    return render(request, 'main/construction/construction_south.html')


def waterboardcentralpage(request):
    return render(request, 'main/waterboard/waterboard_central.html')


def waterboardnorthpage(request):
    return render(request, 'main/waterboard/waterboard_north.html')


def waterboardsouthpage(request):
    return render(request, 'main/waterboard/waterboard_south.html')
