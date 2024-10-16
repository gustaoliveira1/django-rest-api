from django.urls import path
from usuarios.views import UsuarioRegisterView

urlpatterns = [
    path('', UsuarioRegisterView.as_view(), name="user_register"),
]