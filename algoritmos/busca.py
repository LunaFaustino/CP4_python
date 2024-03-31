
class Busca:

    @staticmethod
    def busca_sequencial(lista, valor):
        for indice, elemento in enumerate(lista):
            if elemento == valor:
                return indice
        return -1

    @staticmethod
    def busca_binaria(lista, valor):
        esquerda, direita = 0, len(lista) - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if lista[meio] == valor:
                return meio
            elif lista[meio] < valor:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return -1