from os import system
from funcoes import *

def main():
    system('clear')
    receberCliente()
    while True:
        system('clear')
        opcao = exibirMenu()
        if opcao == '1':
            nProdutos = escolheNumeroProdutos()
            print('Gerando registros...')
            listaProdutos = []
            listaProdutos = criaProdutos(listaProdutos, nProdutos)
            print('Tempo de execução: ')
            input("\n\nAperte ENTER para continuar")
            print('====================== Lista de Produtos =========================\n')
            imprimeProdutos(listaProdutos)
            input("\n\nAperte ENTER para continuar")
            while True:
                criterioOrdenacao = exibeMenuOrdenacao()
                if criterioOrdenacao == 1:
                    print('Ordena por ordem alfabetica')
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 2:
                    print('Ordena por data de lançamento')
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 3:
                    print('Ordena por preço')
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 4:
                    print('Ordena por avaliação')
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 5:
                    print('Ordena por número de unidades vendidas')
                    input("\n\nAperte ENTER para continuar")
                else:
                    break
        else:
            system('clear')
            print('Encerrando programa...')
            print('Volte sempre!')
            break



main()