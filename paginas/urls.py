from django.urls import path
from . import views
from .views import PaginaInicial, HomeView

app_name = "paginas"

urlpatterns = [

    path("", PaginaInicial.as_view(), name='inicio'),
    path("descartezap", HomeView.as_view(), name='home'),
    # path("", views.LoginView.as_view(), name='login'),
    # path("", views.SobreView.as_view(), name="home"),

]
