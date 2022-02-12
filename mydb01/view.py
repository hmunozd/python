from pickle import FALSE
from django.shortcuts import render
from django.shortcuts import redirect
from .extras.database import Conexion
from .extras.autores import Autores, AutoresDao
from .forms import IngresarAutor, EditarAutor

# Create your views here.
def mostrar_index(request):

    autorDao = AutoresDao()
    autorDao.conectarse()

    autorDao.createTabla()
    autorDao.getAll()
    autores = Autores()
    enviado = False
    if request.method == 'POST':
        formulario = IngresarAutor(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            autores = Autores(datos['nombre'], datos['apellido'], datos['celular'], datos['email'])
            autorDao.setCreate(autores)
            autorDao.getAll()
            enviado = True
        else:
            enviado = False
    else:
        formulario = IngresarAutor()
        

    autorDao.db.cerrar_con()
    context = {
        'h': 'Hello my Friend!!',
        'db': autorDao.db,
        'autores': autorDao.db_autores,
        'formulario': formulario,
        'enviado': enviado,
    }
    
    return render(
        request, 
        'mydb01/autor.html',
        context,    
    )

def update_autores(request, record_id):

    autorDao = AutoresDao()
    autorDao.conectarse()
    autores = Autores()

    enviado = False
    if request.method == 'POST':
        print('Autores')
        formulario = EditarAutor(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            autores = Autores(datos['nombre'], datos['apellido'], datos['celular'], datos['email'], datos['id'])
            autorDao.setUpdate(autores)
            enviado = True
        else:
            enviado = False
    else:
        autor = autorDao.getRegistro(record_id)
        data = {
            'nombre': autor.nombre,
            'apellido': autor.apellido,
            'celular': autor.celular,
            'email': autor.email,
            'id': autor.id,
        }
        formulario = EditarAutor(data)
        
    autorDao.db.cerrar_con()

    context = {
        'h': 'Hello Autor!!',
        'db': autorDao.db,
        'formulario': formulario,
        'enviado': enviado,
    }
    return render(
        request, 
        'mydb01/aeditar.html',
        context,    
    )

def update_autores2(request):

    autorDao = AutoresDao()
    autorDao.conectarse()
    autores = Autores()

    enviado = False
    if request.method == 'POST':
        formulario = EditarAutor(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            autores = Autores(datos['nombre'], datos['apellido'], datos['celular'], datos['email'], datos['id'])
            autorDao.setUpdate(autores)
            enviado = True
        else:
            print(formulario.errors)
            enviado = False
        
    autorDao.db.cerrar_con()

    context = {
        'h': 'Hello my Friend!!',
        'db': autorDao.db,
        'autores': autores,
        'formulario': formulario,
        'enviado': enviado,
    }
    return render(
        request, 
        'mydb01/aeditar.html',
        context,    
    )

def delete_autores(request, record_id):
    autorDao = AutoresDao()
    autorDao.conectarse()
    autorDao.setDelete(record_id)
    autorDao.getAll()
    enviado = False
    if request.method == 'POST':
        formulario = IngresarAutor(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            autores = Autores(datos['nombre'], datos['apellido'], datos['celular'], datos['email'])
            autorDao.setCreate(autores)
            autorDao.getAll()
            enviado = True
            return redirect('mydb:iraindex')
        else:
            enviado = False
    else:
        formulario = IngresarAutor()
    autorDao.db.cerrar_con()
    context = { 'h': 'Hello my Friend!!',
        'db': autorDao.db,
        'autores': autorDao.db_autores,
        'formulario': formulario,
        'enviado': enviado,
        'eliminado': True,
    }
    return render(request, 'mydb01/autor.html', context)