from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path('detalhes/<int:id>/', views.detalhes_veiculo, name='detalhes_veiculo'),

]