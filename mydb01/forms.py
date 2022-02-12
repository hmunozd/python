from tkinter import Widget
from django import forms

class IngresarTutorial(forms.Form):
    titulo = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter titulo'})
    autor = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter autor'})
    creado = forms.CharField(widget = forms.SelectDateWidget(), error_messages={'required': 'Please enter date'})

class EditarTutorial(forms.Form):
    titulo = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter titulo'})
    autor = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}), error_messages={'required': 'Please enter autor'})
    creado = forms.CharField(widget = forms.SelectDateWidget(), error_messages={'required': 'Please enter date'})
    id = forms.CharField(widget = forms.HiddenInput())

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