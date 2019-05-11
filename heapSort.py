from os import system

def heapifyOrdemAlfabetica(listaProdutos, tamanho, i):
    raiz = i 
    filhoEsquerda = (2*i) + 1
    filhoDireita = (2*i) + 2

    # confere existencia do filho da esquerda e se é maior que a raiz
    if filhoEsquerda < tamanho and listaProdutos[raiz].nome < listaProdutos[filhoEsquerda].nome:
        raiz = filhoEsquerda

    # confere existencia do filho da direita e se é maior que a raiz
    if filhoDireita < tamanho and listaProdutos[raiz].nome < listaProdutos[filhoDireita].nome:
        raiz = filhoDireita
    
    if raiz != i:
        #swap
        aux = listaProdutos[i]
        listaProdutos[i] = listaProdutos[raiz]
        listaProdutos[raiz] = aux

        #heapify para a nova raiz
        heapifyOrdemAlfabetica(listaProdutos, tamanho, raiz)

def heapifyDataLancamento(listaProdutos, tamanho, i):
    raiz = i 
    filhoEsquerda = (2*i) + 1
    filhoDireita = (2*i) + 2

    # confere existencia do filho da esquerda e se é maior que a raiz
    if filhoEsquerda < tamanho and listaProdutos[raiz].dataLancamento > listaProdutos[filhoEsquerda].dataLancamento:
        raiz = filhoEsquerda

    # confere existencia do filho da direita e se é maior que a raiz
    if filhoDireita < tamanho and listaProdutos[raiz].dataLancamento > listaProdutos[filhoDireita].dataLancamento:
        raiz = filhoDireita
    
    if raiz != i:
        #swap
        aux = listaProdutos[i]
        listaProdutos[i] = listaProdutos[raiz]
        listaProdutos[raiz] = aux

        #heapify para a nova raiz
        heapifyDataLancamento(listaProdutos, tamanho, raiz)

def heapifyPreco(listaProdutos, tamanho, i):
    raiz = i 
    filhoEsquerda = (2*i) + 1
    filhoDireita = (2*i) + 2

    # confere existencia do filho da esquerda e se é maior que a raiz
    if filhoEsquerda < tamanho and listaProdutos[raiz].preco < listaProdutos[filhoEsquerda].preco:
        raiz = filhoEsquerda

    # confere existencia do filho da direita e se é maior que a raiz
    if filhoDireita < tamanho and listaProdutos[raiz].preco < listaProdutos[filhoDireita].preco:
        raiz = filhoDireita
    
    if raiz != i:
        #swap
        aux = listaProdutos[i]
        listaProdutos[i] = listaProdutos[raiz]
        listaProdutos[raiz] = aux

        #heapify para a nova raiz
        heapifyPreco(listaProdutos, tamanho, raiz)
    
def heapifyAvaliacao(listaProdutos, tamanho, i):
    raiz = i 
    filhoEsquerda = (2*i) + 1
    filhoDireita = (2*i) + 2

    # confere existencia do filho da esquerda e se é maior que a raiz
    if filhoEsquerda < tamanho and listaProdutos[raiz].avaliacao > listaProdutos[filhoEsquerda].avaliacao:
        raiz = filhoEsquerda

    # confere existencia do filho da direita e se é maior que a raiz
    if filhoDireita < tamanho and listaProdutos[raiz].avaliacao > listaProdutos[filhoDireita].avaliacao:
        raiz = filhoDireita
    
    if raiz != i:
        #swap
        aux = listaProdutos[i]
        listaProdutos[i]= listaProdutos[raiz]
        listaProdutos[raiz] = aux

        #heapify para a nova raiz
        heapifyAvaliacao(listaProdutos, tamanho, raiz)

def heapifyUnidadesVendidas(listaProdutos, tamanho, i):
    raiz = i 
    filhoEsquerda = (2*i) + 1
    filhoDireita = (2*i) + 2

    # confere existencia do filho da esquerda e se é maior que a raiz
    if filhoEsquerda < tamanho and listaProdutos[raiz].numeroVendas > listaProdutos[filhoEsquerda].numeroVendas:
        raiz = filhoEsquerda

    # confere existencia do filho da direita e se é maior que a raiz
    if filhoDireita < tamanho and listaProdutos[raiz].numeroVendas > listaProdutos[filhoDireita].numeroVendas:
        raiz = filhoDireita
    
    if raiz != i:
        #swap
        aux = listaProdutos[i]
        listaProdutos[i] = listaProdutos[raiz]
        listaProdutos[raiz] = aux

        #heapify para a nova raiz
        heapifyUnidadesVendidas(listaProdutos, tamanho, raiz)

def heapifyCustoBeneficio(listaProdutos, tamanho, i): #Max_Heap
    raiz = i 
    filhoEsquerda = (2*i) + 1
    filhoDireita = (2*i) + 2

    # confere existencia do filho da esquerda e se é maior que a raiz
    if filhoEsquerda < tamanho and ((listaProdutos[raiz].avaliacao > listaProdutos[filhoEsquerda].avaliacao) \
                                    or (listaProdutos[raiz].avaliacao == listaProdutos[filhoEsquerda].avaliacao
                                    and listaProdutos[raiz].preco < listaProdutos[filhoEsquerda].preco)):
        raiz = filhoEsquerda

    # confere existencia do filho da direita e se é maior que a raiz
    if filhoDireita < tamanho and ((listaProdutos[raiz].avaliacao > listaProdutos[filhoDireita].avaliacao) \
                                    or (listaProdutos[raiz].avaliacao == listaProdutos[filhoDireita].avaliacao
                                    and listaProdutos[raiz].preco < listaProdutos[filhoDireita].preco)):
        raiz = filhoDireita
    
    if raiz != i:
        #swap
        aux = listaProdutos[i]
        listaProdutos[i] = listaProdutos[raiz]
        listaProdutos[raiz] = aux

        #heapify para a nova raiz
        heapifyCustoBeneficio(listaProdutos, tamanho, raiz)

def heapSort(listaProdutos, criterioOrdenacao): 
    tamanho = len(listaProdutos)

    if criterioOrdenacao == 1: #Max_Heap
        # Constroi Heap
        for i in range(tamanho, -1, -1): #Faz do final para o início do vetor
            heapifyOrdemAlfabetica(listaProdutos, tamanho, i)

        # Remove a Raiz
        for i in range(tamanho-1, 0, -1):
            aux = listaProdutos[i]
            listaProdutos[i] = listaProdutos[0]
            listaProdutos[0] = aux

            heapifyOrdemAlfabetica(listaProdutos, i, 0)

    elif criterioOrdenacao == 2: #Min_Heap
        # Constroi Heap
        for i in range(tamanho, -1, -1): #Faz do final para o início do vetor
            heapifyDataLancamento(listaProdutos, tamanho, i)

        # Remove a Raiz
        for i in range(tamanho-1, 0, -1):
            aux = listaProdutos[i]
            listaProdutos[i] = listaProdutos[0]
            listaProdutos[0] = aux

            heapifyDataLancamento(listaProdutos, i, 0)

    elif criterioOrdenacao == 3: #Max_Heap
        # Constroi Heap
        for i in range(tamanho, -1, -1): #Faz do final para o início do vetor
            heapifyPreco(listaProdutos, tamanho, i)

        # Remove a Raiz
        for i in range(tamanho-1, 0, -1):
            aux = listaProdutos[i]
            listaProdutos[i] = listaProdutos[0]
            listaProdutos[0] = aux

            heapifyPreco(listaProdutos, i, 0)

    elif criterioOrdenacao == 4: #Min_Heap
        # Constroi Heap
        for i in range(tamanho, -1, -1): #Faz do final para o início do vetor
            heapifyAvaliacao(listaProdutos, tamanho, i)

        # Remove a Raiz
        for i in range(tamanho-1, 0, -1):
            aux = listaProdutos[i]
            listaProdutos[i] = listaProdutos[0]
            listaProdutos[0] = aux

            heapifyAvaliacao(listaProdutos, i, 0)

    elif criterioOrdenacao == 5: #Min_Heap
        # Constroi Heap
        for i in range(tamanho, -1, -1): #Faz do final para o início do vetor
            heapifyUnidadesVendidas(listaProdutos, tamanho, i)

        # Remove a Raiz
        for i in range(tamanho-1, 0, -1):
            aux = listaProdutos[i]
            listaProdutos[i] = listaProdutos[0]
            listaProdutos[0] = aux

            heapifyUnidadesVendidas(listaProdutos, i, 0)
    else: 
        # Constroi Heap
        for i in range(tamanho, -1, -1): #Faz do final para o início do vetor
            heapifyCustoBeneficio(listaProdutos, tamanho, i)

        # Remove a Raiz
        for i in range(tamanho-1, 0, -1):
            aux = listaProdutos[i]
            listaProdutos[i] = listaProdutos[0]
            listaProdutos[0] = aux

            heapifyCustoBeneficio(listaProdutos, i, 0)
    
    return listaProdutos
   