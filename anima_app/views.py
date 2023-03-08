from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, CreateView, FormView
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'anima_app/home.html')

def about(request):
    return render(request, 'anima_app/about.html')

def services(request):
    return render(request, 'anima_app/services.html')

class ContactView(FormView):
    template_name = 'anima_app/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('anima_app:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

def success(request):
    return render(request, 'anima_app/success.html')