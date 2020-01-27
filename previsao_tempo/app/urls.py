from django.urls import path
from .views import *


urlpatterns = [
    path('consultar_clima', consultar_clima, name='consultar_clima'),
    path('consultar_historico', consultar_historico, name='consultar_historico'),
]
