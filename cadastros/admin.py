from django.contrib import admin
# Register your models here.

from .models import Doadores, Doacao

admin.site.register(Doadores)
admin.site.register(Doacao)
