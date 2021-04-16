from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView
from .models import Admin,Manager,User
from django.shortcuts import render

class ManagerCreateView(CreateView):
    model = User
    form_class = forms.ManagerCreateForm
    template_name = 'accounts/signup_form.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'manager'
        return context
    
class AdminCreateView(CreateView):
    model = User
    form_class = forms.AdminCreateForm
    template_name = 'accounts/signup_form.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'admin'
        return context
    
def SignUpView(request):
    return render(request,template_name='accounts/signup.html')