from django.urls import path
from . import views
from .views import DoadoresCreate, DoacaoCreate
from .views import DoadorUpdate
from .views import DoadoresList, DoacaoList
from django.contrib.auth import views as auth_views

app_name = "cadastros"

urlpatterns = [

    path('', auth_views.LoginView.as_view(template_name='account/login.html'), name='cadastrar'),
    # path("Descartezap", HomeView.as_view(), name='home'),
    path('cadastros/Doadores/', DoadoresCreate.as_view(), name="cadastrar-doadores"),
    path('atualizar-dados/', DoadorUpdate.as_view(), name="atualizar-dados"),
    path('cadastros/doacao/', DoacaoCreate.as_view(), name="cadastrar-doacao"),
    path('editar/doadores/<int:pk>/', DoadorUpdate.as_view(), name='editar-doadores'),
    path('listar/doadores/', DoadoresList.as_view(), name='listar-doadores'),
    path('listar/doacao/', DoacaoList.as_view(), name='listar-doacao'),
    # path("", views.SobreView.as_view(), name="home"),

]
