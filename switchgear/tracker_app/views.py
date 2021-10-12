from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView

from tracker_app.forms import WorkerCreationForm


class Main(View):
    def get(self, request):
        return render(request, 'home.html')


class SignUpView(CreateView):
    form_class = WorkerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
