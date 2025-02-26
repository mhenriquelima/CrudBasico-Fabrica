from django import forms
from .models import Usuario


""" first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=15) """
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password', 'age', 'birth_date', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': 'Senha',
            'age': 'Idade',
            'birth_date': 'Data de Nascimento',
            'phone': 'Telefone',
        }
        