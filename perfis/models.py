from django.db import models
from email import email

class Perfil(object):
    def __init__(self, nome='', email='', telefone='', nome_empresa=''):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa
        
    def __str__(self):
        return 'nome: %s \t email: %s \t telefone: %s \t empresa: %s' % (self.nome, self.email, self.telefone, self.nome_empresa)