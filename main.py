from os import system
import time
from funcoes import *
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
            inicio = time.time()
            listaProdutos = criaProdutos(listaProdutos, nProdutos)
            fim = time.time()
            print('Tempo de execução: {:.6f} s'.format (fim - inicio))
            input("\n\nAperte ENTER para continuar")
            print('====================== Lista de Produtos =========================\n')
            imprimeProdutos(listaProdutos)
            input("Aperte ENTER para continuar")
            while True:
                criterioOrdenacao = exibeMenuOrdenacao()
                if criterioOrdenacao == 1:
                    print('----------------- Ordem Alfabética ---------------------------')
                    inicioHeapOrdemAlfabetica = time.time()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapOrdemAlfabetica = time.time()
                    imprimeProdutos(listaProdutos)
                    print('Tempo de execução: {:.6f} s'.format (fimHeapOrdemAlfabetica - inicioHeapOrdemAlfabetica))
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 2:
                    print('----------------- Mais Recentes ---------------------------')
                    inicioHeapDataLancamento = time.time()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapDataLancamento = time.time()
                    imprimeProdutos(listaProdutos)
                    print('Tempo de execução: {:.6f} s'.format (fimHeapDataLancamento - inicioHeapDataLancamento))
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 3:
                    print('----------------- Mais Baratos ---------------------------')
                    inicioHeapPreco = time.time()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapPreco = time.time()
                    imprimeProdutos(listaProdutos)
                    print('Tempo de execução: {:.6f} s'.format (fimHeapPreco - inicioHeapPreco))
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 4:
                    print('----------------- Melhores Avaliados ---------------------------')
                    inicioHeapAvaliacao = time.time()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapAvaliacao = time.time()
                    imprimeProdutos(listaProdutos)
                    print('Tempo de execução: {:.6f} s'.format (fimHeapAvaliacao - inicioHeapAvaliacao))
                    input("\n\nAperte ENTER para continuar")
                elif criterioOrdenacao == 5:
                    print('----------------- Mais Vendidos ---------------------------')
                    inicioHeapUnidadesVendidas = time.time()
                    listaProdutos = heapSort(listaProdutos, criterioOrdenacao)
                    fimHeapUnidadesVendidas = time.time()
                    imprimeProdutos(listaProdutos)
                    print('Tempo de execução: {:.6f} s'.format (fimHeapUnidadesVendidas - inicioHeapUnidadesVendidas))
                    input("\n\nAperte ENTER para continuar")
                else:
                    break
        else:
            system('clear')
            print('Encerrando programa...')
            print('Volte sempre!')
            break



main()