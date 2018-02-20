from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')