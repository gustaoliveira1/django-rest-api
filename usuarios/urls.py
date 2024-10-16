from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from usuarios.views import UsuarioRegisterView, UsuarioDetailsView

urlpatterns = [
    path('', UsuarioRegisterView.as_view(), name="user_register"),
    path('<int:pk>/', UsuarioDetailsView.as_view(), name="user_details"),
    path('auth/', TokenObtainPairView.as_view(), name="token_obtain_pair'"),
]