from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Filter

def index(request):
	filters = Filter.objects.all()
	return render(request, 'index.html', {'filters': filters} )

def about(request):
	return render(request, 'about.html')

def results(request):
	return render(request, 'results.html')

def profile(request):
	return render(request, 'profile.html')


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
