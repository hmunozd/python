from pickle import FALSE
from django.shortcuts import render
from django.shortcuts import redirect
from .extras.database import Conexion
from .extras.autores import AutoresDao
from .forms import IngresarTutorial, EditarTutorial

def mis_tutoriales(request, record_id):

    autoresDao = AutoresDao()
    autoresDao.conectarse()
    autor = autoresDao.getRegistro(record_id)

    tutoriales = autoresDao.mis_tutoriales(record_id)
        
    autoresDao.db.cerrar_con()

    context = {
        'h': 'Hello my Friend!!',
        'db': autoresDao.db,
        'tutoriales': tutoriales,
        'autor': autor,
    }
    return render(
        request, 
        'mydb01/autores/mis_tutoriales.html',
        context,    
    )
