from django.shortcuts import render
from BookingSystem.models import Customer
from BookingSystem.registration import CustomerForm
from django.shortcuts import redirect
from django.contrib import messages


def home(request):
    return render(request, 'BookingSystem/home.html')


def about(request):
    return render(request, 'BookingSystem/about.html')


def news(request):
    return render(request, 'BookingSystem/news.html')


def contact(request):
    return render(request, 'BookingSystem/contact.html')


def registration(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            First_Name = form.cleaned_data.get('First_Name')
            messages.success(request, f'Account created for {First_Name}!')
        return redirect('/')
    return render(request, 'BookingSystem/register.html', {'form': form})
