from django.urls import path
from licoes.views import LicoesRegisterView, LicoesRetriveView

urlpatterns = [
    path('', LicoesRegisterView.as_view()),
    path('<int:pk>/', LicoesRetriveView.as_view()),
]