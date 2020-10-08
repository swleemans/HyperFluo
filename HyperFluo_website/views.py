from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request: HttpRequest):
    return render(request, "index.html")


def about(request: HttpRequest):
    return render(request, "about.html")


def contact(request: HttpRequest):
    return render(request, "contact.html")



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
 