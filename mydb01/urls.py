from django.contrib import admin
from django.urls import path
from . import views, view

app_name = 'mydb'

urlpatterns = [
    path('', views.mostrar_index, name='index'),
    path('index/', views.mostrar_index, name='irindex'),
    path('editar/<int:record_id>', views.update_tutorial, name='editar'),
    path('editar/', views.update_tutorial2, name='editar'),
    path('delete/<int:record_id>', views.delete_tutorial, name='delete'),
    path('autor', view.mostrar_index, name='autor'),
    path('aindex/', view.mostrar_index, name='iraindex'),
    path('aeditar/<int:record_id>', view.update_autores, name='aeditar'),
    path('aeditar/', view.update_autores2, name='aeditar'),
    path('adelete/<int:record_id>', view.delete_autores, name='adelete'),
]
