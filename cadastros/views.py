from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .models import Doadores, Doacao
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UsuarioForm
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError


def formdoar(request):
    urldoar = reverse('paginas:index.html')


class FormCadastro(TemplateView):
    template_name = 'cadastrar/form.html'


class DoadoresCreate(CreateView):
    template_name = 'cadastrar/doador.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('paginas:home')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Doadores')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        Doadores.objects.create(username=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de Novo Usuário"
        context['Botao'] = "Cadastrar"
        return context


class DoacaoCreate(CreateView):
    model = Doacao
    fields = ['quantidade', 'descricao']
    template_name = 'cadastrar/doacao.html'
    success_url = reverse_lazy('paginas:home')

    def form_valid(self, form):
        form.instance.username = self.request.user
        url = super().form_valid(form)
        return url


#################### UPDATE ########################

class DoadorUpdate(UpdateView):
    template_name = 'cadastrar/doador.html'
    model = Doadores
    fields = ['nome', 'sobrenome', 'dataNascimento', 'endereco', 'numero', 'bairro', 'cidade', 'telefonefixo',
              'celular']
    success_url = reverse_lazy('paginas:home')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Doadores, username=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de Novo Usuário"
        context['Botao'] = "Atualizar"

        return context


#################### LISTA ########################

class DoadoresList(ListView):
    model = Doadores
    template_name = 'cadastrar/listas/doadores.html'

    def get_queryset(self):
        self.object_list = Doadores.objects.filter(username=self.request.user)
        return self.object_list


class DoacaoList(ListView, Doacao):
    model = Doacao
    template_name = 'cadastrar/listas/doacao.html'

    def get_queryset(self):
        self.object_list = Doacao.objects.filter(username=self.request.user)
        return self.object_list
