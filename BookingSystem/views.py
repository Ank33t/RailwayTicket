from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from BookingSystem.models import Train
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    context = {
        'trains': Train.objects.all()
    }
    return render(request, 'BookingSystem/home.html', context)


class TrainListVIew(ListView):
    model = Train
    template_name = 'BookingSystem/home.html'
    context_object_name = 'trains'


class TrainDetailVIew(DetailView):
    model = Train


class TrainCreateVIew(LoginRequiredMixin, CreateView):
        model = Train
        fields = ['Train_Name', 'Train_Type', 'Source', 'Destination', 'Travel_Time', 'General_Class', 'First_Class']

        def form_valid(self, form):
            return super().form_valid(form)


class TrainUpdateVIew(LoginRequiredMixin, UpdateView):
    model = Train
    fields = ['Train_Name', 'Train_Type', 'Source', 'Destination', 'Travel_Time', 'General_Class', 'First_Class']

    def form_valid(self, form):
        return super().form_valid(form)


class TrainDeleteVIew(LoginRequiredMixin, DeleteView):
    model = Train
    success_url = '/'


def about(request):
    return render(request, 'BookingSystem/about.html')


def contact(request):
    return render(request, 'BookingSystem/contact.html')

