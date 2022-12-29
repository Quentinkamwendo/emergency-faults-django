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
    return render(request, 'main/northern_faults.html')


def southfaultpage(request):
    return render(request, 'main/southern_faults.html')


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


def deletecentralescompage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('escom-central')
    return render(request, 'main/delete/delete_escom_central.html', {'reports': reports})


def escomnorthpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escom-north')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}

    return render(request, 'main/escom/escom_north.html', context)


def deletenorthescompage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('escom-north')
    return render(request, 'main/delete/delete_escom_north.html', {'reports': reports})


def escomsouthpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escom-south')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/escom/escom_south.html', context)


def deletesouthescompage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('escom-south')
    return render(request, 'main/delete/delete_escom_south.html', {'reports': reports})


def constructioncentralpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('construction-central')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/construction/construction_central.html', context)


def deletecentralconstructionpage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('construction-central')
    return render(request, 'main/delete/delete_construction_central.html', {'reports': reports})

def constructionnorthpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('construction-north')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/construction/construction_north.html', context)


def deletenorthconstructionpage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('construction-north')
    return render(request, 'main/delete/delete_construction_north.html', {'reports': reports})


def constructionsouthpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('construction-south')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/construction/construction_south.html', context)


def deletesouthconstructionpage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('construction-south')
    return render(request, 'main/delete/delete_construction_south.html', {'reports': reports})


def waterboardcentralpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waterboard-central')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/waterboard/waterboard_central.html', context)


def deletecentralwaterboardpage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('waterboard-central')
    return render(request, 'main/delete/delete_waterboard_central.html', {'reports': reports})


def waterboardnorthpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waterboard-north')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/waterboard/waterboard_north.html', context)


def deletenorthwaterboardpage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('waterboard-north')
    return render(request, 'main/delete/delete_waterboard_north.html', {'reports': reports})


def waterboardsouthpage(request):
    reports = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waterboard-south')
    report_count = reports.count()
    context = {'reports': reports, 'form': form, 'report_count': report_count}
    return render(request, 'main/waterboard/waterboard_south.html', context)


def deletesouthwaterboardpage(request, pk):
    reports = Report.objects.get(id=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('waterboard-south')
    return render(request, 'main/delete/delete_waterboard_south.html', {'reports': reports})
