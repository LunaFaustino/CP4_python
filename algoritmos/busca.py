
class Busca:

    @staticmethod
    def busca_sequencial(lista, valor_procurado):
        indice = 0
        for numero in lista:
            if numero == valor_procurado:
                return indice
            indice = indice + 1
        return -1

    @staticmethod
    def busca_binaria(lista, elemento):
        inicio = 0
        fim = len(lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            if lista[meio] == elemento:
                return meio
            elif lista[meio] < elemento:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1