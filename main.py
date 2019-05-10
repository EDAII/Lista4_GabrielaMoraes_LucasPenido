from os import system
from funcoes import *
from radixSortLSD import *
from time import clock
from heapSort import *
from copy import deepcopy

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
                    listaProdutosHeap = deepcopy(listaProdutos)
                    listaProdutosRadixLSD = deepcopy(listaProdutos)

                    inicioHeapOrdemAlfabetica = clock()
                    listaProdutos = heapSort(listaProdutosHeap, criterioOrdenacao)
                    fimHeapOrdemAlfabetica = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapOrdemAlfabetica - inicioHeapOrdemAlfabetica))

                    start_time = clock()
                    radixSortLSD(listaProdutosRadixLSD, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (end_time - start_time))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 2:
                    print('----------------- Mais Recentes ---------------------------')
                    listaProdutosHeap = deepcopy(listaProdutos)
                    listaProdutosRadixLSD = deepcopy(listaProdutos)

                    inicioHeapDataLancamento = clock()
                    listaProdutos = heapSort(listaProdutosHeap, criterioOrdenacao)
                    fimHeapDataLancamento = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapDataLancamento - inicioHeapDataLancamento))

                    start_time = clock()
                    radixSortLSD(listaProdutosRadixLSD, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (end_time - start_time))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 3:
                    print('----------------- Mais Baratos ---------------------------')
                    listaProdutosHeap = deepcopy(listaProdutos)
                    listaProdutosRadixLSD = deepcopy(listaProdutos)

                    inicioHeapPreco = clock()
                    listaProdutos = heapSort(listaProdutosHeap, criterioOrdenacao)
                    fimHeapPreco = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapPreco - inicioHeapPreco))

                    start_time = clock()
                    radixSortLSD(listaProdutosRadixLSD, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (end_time - start_time))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 4:
                    print('----------------- Melhores Avaliados ---------------------------')
                    listaProdutosHeap = deepcopy(listaProdutos)
                    listaProdutosRadixLSD = deepcopy(listaProdutos)

                    inicioHeapAvaliacao = clock()
                    listaProdutos = heapSort(listaProdutosHeap, criterioOrdenacao)
                    fimHeapAvaliacao = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapAvaliacao - inicioHeapAvaliacao))

                    start_time = clock()
                    radixSortLSD(listaProdutosRadixLSD, criterioOrdenacao)
                    end_time = clock()
                    print('Tempo de execução Radix LSD Sort: {:.6f} s'.format (fimHeapAvaliacao - inicioHeapAvaliacao))

                    input("\n\nAperte ENTER para continuar")
                    imprimeProdutos(listaProdutos)
                elif criterioOrdenacao == 5:
                    print('----------------- Mais Vendidos ---------------------------')
                    listaProdutosHeap = deepcopy(listaProdutos)
                    listaProdutosRadixLSD = deepcopy(listaProdutos)

                    inicioHeapUnidadesVendidas = clock()
                    listaProdutos = heapSort(listaProdutosHeap, criterioOrdenacao)
                    fimHeapUnidadesVendidas = clock()
                    print('Tempo de execução Heap Sort: {:.6f} s'.format (fimHeapUnidadesVendidas - inicioHeapUnidadesVendidas))

                    start_time = clock()
                    radixSortLSD(listaProdutosRadixLSD, criterioOrdenacao)
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
