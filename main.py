from os import system
from funcoes import *
from radixSortLSD import *
from time import clock

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
            start_time = clock()
            listaProdutos = criaProdutos(listaProdutos, nProdutos)
            end_time = clock()
            print('Tempo de execução: ')
            elapsed_time = end_time - start_time
            print(elapsed_time)
            input("\n\nAperte ENTER para continuar")
            print('====================== Lista de Produtos =========================\n')
            imprimeProdutos(listaProdutos)
            input("\n\nAperte ENTER para continuar")
            while True:
                criterioOrdenacao = exibeMenuOrdenacao()
                if criterioOrdenacao == 1:
                    print('Ordena por ordem alfabetica')
                    start_time = clock()
                    radixSortLSDNomeProduto(listaProdutos)
                    end_time = clock()
                    print('Tempo total :')
                    print(end_time - start_time)
                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 2:
                    print('Ordena por data de lançamento')
                    start_time = clock()
                    radixSortLSDData(listaProdutos)
                    end_time = clock()
                    print('Tempo total :')
                    print(end_time - start_time)
                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 3:
                    print('Ordena por preço')
                    start_time = clock()
                    radixSortLSDPreco(listaProdutos)
                    end_time = clock()
                    print('Tempo total :')
                    print(end_time - start_time)
                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 4:
                    print('Ordena por avaliação')
                    start_time = clock()
                    radixSortLSDAvaliacao(listaProdutos)
                    end_time = clock()
                    print('Tempo total :')
                    print(end_time - start_time)
                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 5:
                    print('Ordena por número de unidades vendidas')
                    start_time = clock()
                    radixSortLSDNumeroUnidades(listaProdutos)
                    end_time = clock()
                    print('Tempo total :')
                    print(end_time - start_time)
                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                else:
                    break
        else:
            system('clear')
            print('Encerrando programa...')
            print('Volte sempre!')
            break



main()
