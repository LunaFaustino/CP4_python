import sys
import os
from algoritmos.ordenacao import Ordenacao
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import random

def listas():
    lista_ordenado_crescente = [3, 7, 33, 59, 71]

    lista_nao_ordenado= [71, 7, 3, 9, 7]

    lista_ordenado_decrescente= [71, 59, 33, 7, 3]

    lista_vazio= []

    lista_unico_elemento= [42]

    lista_elementos_repetidos= [3, 7, 3, 9, 7]

    def lista_aleatoria(tamanho_lista):
        lista_aleatoria = random.sample(range(1, tamanho_lista+1), tamanho_lista) 
        return lista_aleatoria

    dicionario_de_listas = {
        "lista_ordenado_crescente": lista_ordenado_crescente,
        "lista_nao_ordenado": lista_nao_ordenado,
        "lista_ordenado_decrescente": lista_ordenado_decrescente,
        "lista_vazio": lista_vazio,
        "lista_unico_elemento": lista_unico_elemento,
        "lista_elementos_repetidos": lista_elementos_repetidos,
        "lista_aleatoria10": lista_aleatoria(10),
        "lista_aleatoria100": lista_aleatoria(100),
        "lista_aleatoria1000": lista_aleatoria(1000)
    }
    return dicionario_de_listas

class TesteOrdenacao:
    def teste_vetor(vetor):
        print("\n\nVETOR: \n", vetor)
        print("\nOrdenação Buble Sort: ", Ordenacao.bubble_sort(vetor))
        print("\nOrdenação selection_sort: ", Ordenacao.selection_sort(vetor))
        print("\nOrdenação insertion_sort: ", Ordenacao.insertion_sort(vetor))
        print("\nOrdenação merge_sort: ", Ordenacao.merge_sort(vetor))
        print("\nOrdenação quick_sort: ", Ordenacao.quick_sort(vetor))
        return()
    

    


