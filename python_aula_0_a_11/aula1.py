# -*- coding: UTF-8 -*-
def listar(nomes):
  print 'Listando nomes'
  for nome in nomes:
    print nome

def cadastrar(nomes):
  print 'Digite: o nome:'
  nome = raw_input()
  nomes.append(nome)

def menu():
  nomes = []
  escolha = ''
  while(escolha != '0'):    
    print 'Digite 1 para cadastrar, 2 para listar, 3 para remover, 0 para terminar'
    escolha = raw_input()

    if(escolha == '1'):
      cadastrar(nomes)

    if(escolha == '2'):
      listar(nomes)

    if(escolha == '3'):
      remover(nomes)


def remover(nomes):
  print 'Qual nome gostaria de remover?'
  nome = raw_input()
  nomes.remove(nome)

def alterar(nomes):
  print 'Qual nome vc gostaria de alterar?'
  nome_a_alterar = raw_input()

  if(nome_a_alterar in nomes):
    posicao = nomes.index(nome_a_alterar)
    print 'Digite novo nome:'
    nome_novo = raw_input()
    nomes[posicao] = nome_novo

menu()


