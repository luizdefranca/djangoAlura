from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')
def exibir(request, perfil_id):
    print 'ID do perfil recebido: %s' % (perfil_id)
    perfil = Perfil()
    
    if perfil_id == '1':
        perfil = Perfil('Luiz Carlos', 'luizramos@hotmail.com', '679696', 'TCE')
    if perfil_id == '2':
        perfil = Perfil('Romulo Henrique', 'romulo@romulo.com.br', '888888', 'Caelum')
        
    print perfil
    return render(request, 'perfil.html', {"perfil" : perfil})
