from tkinter import Widget
from django import forms

class IngresarTutorial(forms.Form):
    titulo = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}))
    autor = forms.CharField(widget = forms.TextInput( attrs = { 'class': 'form-contorl'}))
    creado = forms.CharField(widget = forms.SelectDateWidget())