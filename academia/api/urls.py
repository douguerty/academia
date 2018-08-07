from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('exercicios', views.ExercicioViewSet)
router.register('treinamentos', views.TreinamentoViewSet)
router.register('logagua', views.LogAguaViewSet)
router.register('logaguadiario', views.LogAguaDiarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
