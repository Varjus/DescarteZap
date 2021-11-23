# from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


class PaginaInicial(TemplateView):
    template_name = "index.html"

    def index(request):
        return render(request, 'index.html')


class HomeView(TemplateView):
    template_name = "home.html"

    def index(request):
        return render(request, 'home.html')
