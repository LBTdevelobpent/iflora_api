from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def pessoasCadastradas(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)