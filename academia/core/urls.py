from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('nova_conta/', views.RegistrationView.as_view(), name='nova_conta'),
    path('info_pessoal/', views.info_pessoal, name='info_pessoal'),
    path('exercicio/', views.exercicio, name='exercicio'),
    path('exercicios/', views.exercicios, name='exercicios'),
    path('exercicio/<int:id>/', views.exercicio_edit, name='exercicio_edit'),
    path('treinamento/', views.treinamento, name='treinamento'),
    path('treinamentos/', views.treinamentos, name='treinamentos'),
    path('treinamento/<int:id>/', views.treinamento_edit, name='treinamento_edit'),
    path('consumo_agua/', views.consumo_agua, name='consumo_agua'),
]