from django.urls import path
from licoes.views import LicoesRegisterView, LicoesRetriveView, edit_content

urlpatterns = [
    path('', LicoesRegisterView.as_view()),
    path('<int:pk>/', LicoesRetriveView.as_view()),
    path('<int:pk>/editar-html/', edit_content),
]