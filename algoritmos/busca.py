
class Busca:

    @staticmethod
    def busca_sequencial(lista, valor_procurado):
        for indice, elemento in enumerate(lista):
            if elemento == valor_procurado:
                return indice
        return -1

    @staticmethod
    def busca_binaria(lista, valor_procurado):
        esquerda, direita = 0, len(lista) - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if lista[meio] == valor_procurado:
                return meio
            elif lista[meio] < valor_procurado:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return -1