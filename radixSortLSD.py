def _maiorNumeroPreco(vetor):
    maiorNumero = 0
    for i in vetor:
        numero = i.preco
        if numero > maiorNumero:
            maiorNumero = numero

    return maiorNumero

def _countingSortPreco(vetor, exp):
    tamVetor = len(vetor)
    resultado = [0] * (tamVetor)
    count = [0] * (10)

    for i in range(0, tamVetor):
        index = int((vetor[i].preco*100/exp)%10)
        count[index] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = tamVetor-1
    while i>=0:
        index = int((vetor[i].preco*100/exp)%10)
        resultado[count[index] - 1] = vetor[i]
        count[index] -= 1
        i -= 1

    i = 0
    for i in range(0,len(vetor)):
        vetor[i] = resultado[i]

def radixSortLSDPreco(vetor):
    max = _maiorNumeroPreco(vetor)

    exp = 1
    while int(max*100/exp) > 0:
        _countingSortPreco(vetor,exp)
        exp *= 10

def _countingSortData(vetor, digito):
    tamVetor = len(vetor)
    resultado = [0] * (tamVetor)
    count = [0] * (123)

    for i in range(0, tamVetor):
        index = str(vetor[i].dataLancamento)[-digito]

        count[ord(index)] += 1

    for i in range(1,123):
        count[i] += count[i-1]

    i = tamVetor-1
    while i>=0:
        index = str(vetor[i].dataLancamento)[-digito]

        resultado[count[ord(index)] - 1] = vetor[i]
        count[ord(index)] -= 1
        i -= 1

    i = 0
    for i in range(0,len(vetor)):
        vetor[i] = resultado[i]

def radixSortLSDData(vetor):

    digitos = 10

    for i in range(1, digitos+1):
        _countingSortData(vetor,i)

def _maiorNumeroAvaliacao(vetor):
    maiorNumero = 0
    for i in vetor:
        numero = i.avaliacao
        if numero > maiorNumero:
            maiorNumero = numero

    return maiorNumero

def _countingSortAvaliacao(vetor, exp):
    tamVetor = len(vetor)
    resultado = [0] * (tamVetor)
    count = [0] * (10)

    for i in range(0, tamVetor):
        index = int((vetor[i].avaliacao/exp)%10)
        count[index] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = tamVetor-1
    while i>=0:
        index = int((vetor[i].avaliacao/exp)%10)
        resultado[count[index] - 1] = vetor[i]
        count[index] -= 1
        i -= 1

    i = 0
    for i in range(0,len(vetor)):
        vetor[i] = resultado[i]

def radixSortLSDAvaliacao(vetor):
    max = _maiorNumeroAvaliacao(vetor)

    exp = 1
    while int(max/exp) > 0:
        _countingSortAvaliacao(vetor,exp)
        exp *= 10

def _maiorNumeroUnidades(vetor):
    maiorNumero = 0
    for i in vetor:
        numero = i.numeroVendas
        if numero > maiorNumero:
            maiorNumero = numero

    return maiorNumero

def _countingSortNumeroUnidades(vetor, exp):
    tamVetor = len(vetor)
    resultado = [0] * (tamVetor)
    count = [0] * (10)

    for i in range(0, tamVetor):
        index = int((vetor[i].numeroVendas/exp)%10)
        count[index] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = tamVetor-1
    while i>=0:
        index = int((vetor[i].numeroVendas/exp)%10)
        resultado[count[index] - 1] = vetor[i]
        count[index] -= 1
        i -= 1

    i = 0
    for i in range(0,len(vetor)):
        vetor[i] = resultado[i]

def radixSortLSDNumeroUnidades(vetor):
    max = _maiorNumeroUnidades(vetor)

    exp = 1
    while int(max/exp) > 0:
        _countingSortNumeroUnidades(vetor,exp)
        exp *= 10

def _maiorQntdDigitos(vetor):
    maiorDigitos = 0
    for i in vetor:
        tam = len(i.nome)
        if tam > maiorDigitos:
            maiorDigitos = tam

    return maiorDigitos

def _countingSortNomeProduto(vetor, digito):
    tamVetor = len(vetor)
    resultado = [0] * (tamVetor)
    count = [0] * (123)

    for i in range(0, tamVetor):
        # print(vetor[i])
        # index = vetor[i][len(vetor[i]) - digito : len(vetor[i]) - (digito - 1)]
        if digito <= len(vetor[i].nome):
            index = vetor[i].nome[-digito]
        else:
            index = vetor[i].nome[0]
        # print(ord(index))
        count[ord(index)] += 1

    for i in range(1,123):
        count[i] += count[i-1]

    i = tamVetor-1
    while i>=0:
        if digito <= len(vetor[i].nome):
            index = vetor[i].nome[-digito]
        else:
            index = vetor[i].nome[0]
        resultado[count[ord(index)] - 1] = vetor[i]
        count[ord(index)] -= 1
        i -= 1

    i = 0
    for i in range(0,len(vetor)):
        vetor[i] = resultado[i]

def radixSortLSDNomeProduto(vetor):

    digitos = _maiorQntdDigitos(vetor)

    for i in range(1, digitos+1):
        _countingSortNomeProduto(vetor,i)

def radixSortLSD(listaProdutos, criterioOrdenacao):

    if criterioOrdenacao == 1:
        radixSortLSDNomeProduto(listaProdutos)

    elif criterioOrdenacao == 2:
        radixSortLSDData(listaProdutos)

    elif criterioOrdenacao == 3:
        radixSortLSDPreco(listaProdutos)

    elif criterioOrdenacao == 4:
        radixSortLSDAvaliacao(listaProdutos)

    else:
        radixSortLSDNumeroUnidades(listaProdutos)
