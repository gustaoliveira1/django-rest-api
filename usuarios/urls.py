from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from usuarios.views import UsuarioRegisterView

urlpatterns = [
    path('', UsuarioRegisterView.as_view(), name="user_register"),
    path('auth/', TokenObtainPairView.as_view(), name="token_obtain_pair'"),
]