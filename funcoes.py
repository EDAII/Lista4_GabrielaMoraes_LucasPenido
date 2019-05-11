import os
import sys
import random
from datetime import date
from faker import Faker

fake = Faker()

class Produto:
    nome: str 
    dataLancamento: date
    preco: float
    avaliacao: int 
    numeroVendas: int

def receberCliente():
    print('Olá! Seja bem vindo a loja EDA2...\n\n')
    print('Os produtos aqui exibidos possuem as seguintes informações:')
    print('---------------------------------------------------------')
    print('| Nome\t\t\t\t\t\t\t|')
    print('| Data de lançamento\t\t\t\t\t|')
    print('| Preço\t\t\t\t\t\t\t|')
    print('| Avaliação\t\t\t\t\t\t|')
    print('| Número de Vendas\t\t\t\t\t|')
    print('---------------------------------------------------------')
    input("\n\nAperte ENTER para continuar")

def exibirMenu():
    print('============== Loja Virtual EDA2 ===================')
    print('1. Acessar vitrine virtual')
    print('0. Sair')
    opcao = str(input('Insira o número da ação que deseja realizar: '))
    opcao = validaEntradaMenu(opcao)
    
    return opcao

def validaEntradaMenu(opcao):
    while opcao != '0' and opcao != '1':
        print('Opção inválida! Digite novamente')
        opcao = str(input('Insira o número da ação que deseja realizar: '))
    return opcao

def escolheNumeroProdutos():
    nProdutos = int(input('\n\nDigite o número de produtos que deseja visualizar: '))
    nProdutos = validaNumeroProdutos(nProdutos)

    return nProdutos

def validaNumeroProdutos(nProdutos):
    while nProdutos <= 0:
        print('Quantidade de produtos inválida! Digite uma quantia maior que 0')
        nProdutos = int(input('Digite o número de produtos que deseja visualizar: '))
    return nProdutos

def criaProdutos(listaProdutos, nProdutos):
    for i in range(0, nProdutos):
        produto = Produto()
        produto.nome = fake.word(ext_word_list=None)
        produto.dataLancamento = fake.date_between(start_date='-1y', end_date='today') 
        produto.preco = round(random.uniform(1.00, 1000.00), 2)
        produto.avaliacao = random.randrange(1, 5)
        produto.numeroVendas = random.randrange(1, 1000000)
        listaProdutos.append(produto)

    return listaProdutos

def imprimeProdutos(listaProdutos):
    for i in range(0, len(listaProdutos)):
        print('\nCaracterísticas do Produto ', i+1,'\n')
        print("Nome do Produto: ", listaProdutos[i].nome)
        print("Data de Lançamento: ", listaProdutos[i].dataLancamento)
        print("Preço: R$ ", listaProdutos[i].preco)
        print("Avaliação: ", listaProdutos[i].avaliacao, ' estrela(s)')
        print("Unidades Vendidas: ", listaProdutos[i].numeroVendas)
        print('\n')

def exibeMenuOrdenacao():
    print('\n\nO que você deseja visualizar ?')
    print('\n1. Produtos em ordem alfabética')
    print('2. Mais recentes')
    print('3. Mais baratos')
    print('4. Melhores avaliados')
    print('5. Mais vendidos')
    print('6. Custo Benefício')
    print('0. Sair')
    criterioOrdenacao = int(input('\nInsira o número da opção: '))
    criterioOrdenacao = validaCriterioOrdenacao(criterioOrdenacao)

    return criterioOrdenacao

def validaCriterioOrdenacao(criterioOrdenacao):
    while criterioOrdenacao < 0 or criterioOrdenacao > 6:
        print('Opção inválida! Digite um número entre 0 e 6')
        criterioOrdenacao = int(input('Insira o número da opção: '))
    return criterioOrdenacao