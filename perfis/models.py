from django.db import models



class Perfil(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=100, null=False)

    def __str__(self):
        return 'nome: %s \t email: %s \t telefone: %s \t empresa: %s' % (self.nome, self.email, self.telefone, self.nome_empresa)
