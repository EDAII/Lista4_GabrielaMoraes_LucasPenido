from os import system
from funcoes import *
from radixSortLSD import *
from time import clock
from heapSort import *

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
            inicio = clock()
            listaProdutos = criaProdutos(listaProdutos, nProdutos)
            fim = clock()
            print('Tempo de execução: {:.6f} s'.format (fim - inicio))
            input("\n\nAperte ENTER para continuar")
            print('====================== Lista de Produtos =========================\n')
            imprimeProdutos(listaProdutos)
            input("Aperte ENTER para continuar")
            while True:
                criterioOrdenacao = exibeMenuOrdenacao()
                if criterioOrdenacao == 1:
                    print('----------------- Ordem Alfabética ---------------------------')

                    inicioHeapOrdemAlfabetica = clock()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapOrdemAlfabetica = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapOrdemAlfabetica - inicioHeapOrdemAlfabetica))

                    start_time = clock()
                    radixSortLSD(listaProdutos, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (end_time - start_time))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 2:
                    print('----------------- Mais Recentes ---------------------------')
                    inicioHeapDataLancamento = clock()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapDataLancamento = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapDataLancamento - inicioHeapDataLancamento))

                    start_time = clock()
                    radixSortLSD(listaProdutos, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (end_time - start_time))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 3:
                    print('----------------- Mais Baratos ---------------------------')
                    inicioHeapPreco = clock()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapPreco = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapPreco - inicioHeapPreco))

                    start_time = clock()
                    radixSortLSD(listaProdutos, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (end_time - start_time))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 4:
                    print('----------------- Melhores Avaliados ---------------------------')
                    inicioHeapAvaliacao = clock()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapAvaliacao = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapAvaliacao - inicioHeapAvaliacao))

                    start_time = clock()
                    radixSortLSD(listaProdutos, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (fimHeapAvaliacao - inicioHeapAvaliacao))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 5:
                    print('----------------- Mais Vendidos ---------------------------')
                    inicioHeapUnidadesVendidas = clock()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapUnidadesVendidas = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapUnidadesVendidas - inicioHeapUnidadesVendidas))

                    start_time = clock()
                    radixSortLSD(listaProdutos, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (end_time - start_time))

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
