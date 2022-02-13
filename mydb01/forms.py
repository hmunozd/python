from tkinter import Widget
from django import forms
from .extras.autores import AutoresDao

class IngresarTutorial(forms.Form):
    titulo = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter titulo'})
    autor = forms.ChoiceField(widget = forms.Select( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter autor'}, choices=(),)
    creado = forms.CharField(widget = forms.SelectDateWidget(), error_messages={'required': 'Please enter date'})

    def __init__ (self, *args, **kwargs):
        super(IngresarTutorial, self).__init__(*args, **kwargs)

        self.fields['autor'] = forms.ChoiceField(
            widget = forms.Select(attrs = { 'class': 'form-contorl'}),
            error_messages={'required': 'Please enter autor'},
            choices=updateAutores(),
        )

class EditarTutorial(forms.Form):
    titulo = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter titulo'})
    autor = forms.ChoiceField(widget = forms.Select( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter autor'}, choices=(),)
    creado = forms.CharField(widget = forms.SelectDateWidget(), error_messages={'required': 'Please enter date'})
    id = forms.CharField(widget = forms.HiddenInput())

    def __init__ (self, *args, **kwargs):
        super(EditarTutorial, self).__init__(*args, **kwargs)

        self.fields['autor'] = forms.ChoiceField(
            widget = forms.Select(attrs = { 'class': 'form-contorl'}),
            error_messages={'required': 'Please enter autor'},
            choices=updateAutores(),
        )

class IngresarAutor(forms.Form):
    nombre = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter nombre'})
    apellido = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter apellido'})
    celular = forms.CharField(widget = forms.NumberInput(attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter celular'})
    email = forms.CharField(widget = forms.EmailInput(attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter email'})

class EditarAutor(forms.Form):
    nombre = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter nombre'})
    apellido = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter apellido'})
    celular = forms.CharField(widget = forms.NumberInput(attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter celular'})
    email = forms.CharField(widget = forms.EmailInput(attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter email'})
    id = forms.CharField(widget = forms.HiddenInput())

def updateAutores():
    autoresDao = AutoresDao()
    autoresDao.conectarse()
    autoresDao.getAll()

    autores = autoresDao.db_autores
    autupla = ()
    list_tupla = list(autupla)

    for auto in autores:
        list_tupla.append((auto.id, auto.nombre))

    autoresDao = AutoresDao()
    autoresDao.conectarse()
    autoresDao.getAll()

    autores = autoresDao.db_autores
    autupla = ()
    list_tupla = list(autupla)
    autoresDao.db.cerrar_con()
    for auto in autores:
        list_tupla.append((auto.id, auto.nombre))

    return tuple(list_tupla)