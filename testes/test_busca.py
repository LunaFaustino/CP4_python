from algoritmos import busca


def busca_numero(vetor, numero):
    print("LISTA: {vetor}")
    indice_sequencial = busca.Busca.busca_sequencial(vetor, numero)
    indice_binaria = busca.Busca.busca_binaria(vetor, numero)

    if indice_sequencial != -1:
        print(f"\n\nNA BUSCA SEQUENCIAL: \n O número {numero} foi encontrado no índice {indice_sequencial}.")
    else:
        print(f"\n\nNA BUSCA SEQUENCIAL: \n O número {numero} não foi encontrado.")

    if indice_binaria != -1:
        print(f"\n\nNA BUSCA BINÁRIA: \n O número {numero} foi encontrado no índice {indice_binaria}.")
    else:
        print(f"\n\nNA BUSCA BINÁRIA: \n O número {numero} não foi encontrado.")
    return()
