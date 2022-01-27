from django.shortcuts import render
from .extras.database import Conexion
from .extras.tutoriales import Tutorial, TutorialDao
from .forms import IngresarTutorial

# Create your views here.
def mostrar_index(request):

    tutorialDao = TutorialDao()
    tutorialDao.conectarse()

    tutorialDao.createTabla()
    tutorialDao.getAll()
    click = False
    enviado = True
    if request.method == 'POST':
        formulario = IngresarTutorial(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            tutorial = Tutorial(datos['titulo'], datos['autor'], datos['creado'])
            tutorialDao.setCreate(tutorial)
            enviado = True
            click = True
        else:
            enviado = False
            print(formulario.errors)
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