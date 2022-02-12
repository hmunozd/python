from pickle import FALSE
from django.shortcuts import render
from django.shortcuts import redirect
from .extras.database import Conexion
from .extras.tutoriales import Tutorial, TutorialDao
from .forms import IngresarTutorial, EditarTutorial

# Create your views here.
def mostrar_index(request):

    tutorialDao = TutorialDao()
    tutorialDao.conectarse()

    tutorialDao.createTabla()
    tutorialDao.getAll()
    tutorial = Tutorial()
    enviado = False
    if request.method == 'POST':
        formulario = IngresarTutorial(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            tutorial = Tutorial(datos['titulo'], datos['autor'], datos['creado'])
            tutorialDao.setCreate(tutorial)
            tutorialDao.getAll()
            enviado = True
        else:
            enviado = False
    else:
        formulario = IngresarTutorial()
        

    tutorialDao.db.cerrar_con()
    context = {
        'h': 'Hello my Friend!!',
        'db': tutorialDao.db,
        'tutoriales': tutorialDao.db_tutoriales,
        'formulario': formulario,
        'enviado': enviado,
    }
    
    return render(
        request, 
        'mydb01/index.html',
        context,    
    )

def update_tutorial(request, record_id):

    tutorialDao = TutorialDao()
    tutorialDao.conectarse()
    tutorial = Tutorial()

    enviado = False
    if request.method == 'POST':
        print('Tutorial')
        formulario = EditarTutorial(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            tutorial = Tutorial(datos['titulo'], datos['autor'], datos['creado'], datos['id'])
            tutorialDao.setUpdate(tutorial)
            enviado = True
        else:
            enviado = False
    else:
        tuto = tutorialDao.getRegistro(record_id)
        data = {
            'titulo': tuto.titulo,
            'autor': tuto.autor,
            'creado': tuto.creado,
            'id': tuto.id,
        }
        formulario = EditarTutorial(data)
        
    tutorialDao.db.cerrar_con()

    context = {
        'h': 'Hello my Friend!!',
        'db': tutorialDao.db,
        'formulario': formulario,
        'enviado': enviado,
    }
    return render(
        request, 
        'mydb01/editar.html',
        context,    
    )

def update_tutorial2(request):

    tutorialDao = TutorialDao()
    tutorialDao.conectarse()
    tutorial = Tutorial()

    enviado = False
    if request.method == 'POST':
        formulario = EditarTutorial(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            tutorial = Tutorial(datos['titulo'], datos['autor'], datos['creado'], datos['id'])
            tutorialDao.setUpdate(tutorial)
            enviado = True
        else:
            print(formulario.errors)
            enviado = False
        
    tutorialDao.db.cerrar_con()

    context = {
        'h': 'Hello my Friend!!',
        'db': tutorialDao.db,
        'tutorial': tutorial,
        'formulario': formulario,
        'enviado': enviado,
    }
    return render(
        request, 
        'mydb01/editar.html',
        context,    
    )

def delete_tutorial(request, record_id):
    tutorialDao = TutorialDao()
    tutorialDao.conectarse()
    tutorialDao.setDelete(record_id)
    tutorialDao.getAll()
    enviado = False
    if request.method == 'POST':
        formulario = IngresarTutorial(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            tutorial = Tutorial(datos['titulo'], datos['autor'], datos['creado'])
            tutorialDao.setCreate(tutorial)
            tutorialDao.getAll()
            enviado = True
            return redirect('mydb:irindex')
        else:
            enviado = False
    else:
        formulario = IngresarTutorial()
    formulario = IngresarTutorial()
    tutorialDao.db.cerrar_con()
    context = { 'h': 'Hello my Friend!!',
        'db': tutorialDao.db,
        'tutoriales': tutorialDao.db_tutoriales,
        'formulario': formulario,
        'enviado': enviado,
        'eliminado': True,
    }
    return render(request, 'mydb01/index.html', context)