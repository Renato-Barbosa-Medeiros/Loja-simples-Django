from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.cria_produto, name='cria_produto'),
    path('edita/<int:pk>/', views.edita_produto, name='edita_produto'),
    path('remove/<int:pk>/', views.remove_produto, name='remove_produto'),

    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.cria_cliente, name='cria_cliente'),
    path('clientes/edita/<int:pk>/', views.edita_cliente, name='edita_cliente'),
    path('clientes/remove/<int:pk>/', views.remove_cliente, name='remove_cliente'),

    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/novo/', views.cria_venda, name='cria_venda'),
    path('vendas/edita/<int:pk>/', views.edita_venda, name='edita_venda'),
    path('vendas/remove/<int:pk>/', views.remove_venda, name='remove_venda'),
]