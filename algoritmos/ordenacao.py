
class Ordenacao:

    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    @staticmethod
    def selection_sort(lista):
        n = len(lista)
        for i in range(n):
            minimo = i
            for j in range(i + 1, n):
                if lista[minimo] > lista[j]:
                    minimo = j
            lista[i], lista[minimo] = lista[minimo], lista[i]
        return lista

    @staticmethod
    def insertion_sort(lista):
        n = len(lista)
        for j in range(1, n):
            chave = lista[j]
            i = j - 1
            while i >= 0 and lista[i] > chave:
                lista[i + 1] = lista[i]
                i = i - 1
            lista[i + 1] = chave

        return lista

    @staticmethod
    def merge_sort(lista):
        if len(lista) > 1:
            meio = len(lista) // 2
            metade1 = lista[:meio]
            metade2 = lista[meio:]

            Ordenacao.merge_sort(metade1)
            Ordenacao.merge_sort(metade2)

            i = j = k = 0

            while i < len(metade1) and j < len(metade2):
                if metade1[i] < metade2[j]:
                    lista[k] = metade1[i]
                    i += 1
                else:
                    lista[k] = metade2[j]
                    j += 1
                k += 1

            while i < len(metade1):
                lista[k] = metade1[i]
                i += 1
                k += 1

            while j < len(metade2):
                lista[k] = metade2[j]
                j += 1
                k += 1
        return lista
    
    @staticmethod
    def quick_sort(lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista) - 1

        if inicio < fim:
            pivot = lista[fim]
            i = inicio - 1
            for j in range(inicio, fim):
                if lista[j] <= pivot:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]
            lista[i + 1], lista[fim] = lista[fim], lista[i + 1]

            pivot_index = i + 1

            Ordenacao.quick_sort(lista, inicio, pivot_index - 1)
            Ordenacao.quick_sort(lista, pivot_index + 1, fim)
        
        return lista
