from algoritmos.busca import Busca
from algoritmos.ordenacao import Ordenacao
import time

class Performance:
    def __init__(self):
        self.lista_ordenada = [i for i in range(10000)]
        self.lista_ordenada.sort()
        self.lista_desordenada = [i for i in range(10000)]
        self.lista_desordenada.reverse()

    def test_performance_busca_sequencial(self):
        print("\nTeste de performance para busca sequencial:\n")
        inicio = time.time()
        Busca.busca_sequencial(self.lista_ordenada, 9999)
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.5f} segundos.")
        inicio = time.time()
        Busca.busca_sequencial(self.lista_desordenada, 9999)
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.5f} segundos.\n")

    def test_performance_busca_binaria(self):
        print("Teste de performance para busca binária:\n")
        inicio = time.time()
        Busca.busca_binaria(self.lista_ordenada, 9999)
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.5f} segundos.")
        inicio = time.time()
        Busca.busca_binaria(self.lista_desordenada, 9999)
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.5f} segundos.\n")

    def test_performance_ordenacao_bubble_sort(self):
        print("Teste de performance para ordenação com Bubble Sort:\n")
        inicio = time.time()
        Ordenacao.bubble_sort(self.lista_ordenada.copy())
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.5f} segundos.")
        inicio = time.time()
        Ordenacao.bubble_sort(self.lista_desordenada.copy())
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.5f} segundos.\n")

    def test_performance_ordenacao_selection_sort(self):
        print("Teste de performance para ordenação com Selection Sort:\n")
        inicio = time.time()
        Ordenacao.selection_sort(self.lista_ordenada.copy())
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.5f} segundos.")
        inicio = time.time()
        Ordenacao.selection_sort(self.lista_desordenada.copy())
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.5f} segundos.\n")

    def test_performance_ordenacao_insertion_sort(self):
        print("Teste de performance para ordenação com Insertion Sort:\n")
        inicio = time.time()
        Ordenacao.insertion_sort(self.lista_ordenada.copy())
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.5f} segundos.")
        inicio = time.time()
        Ordenacao.insertion_sort(self.lista_desordenada.copy())
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.5f} segundos.\n")

    def test_performance_ordenacao_merge_sort(self):
        print("Teste de performance para ordenação com Merge Sort:\n")
        inicio = time.time()
        Ordenacao.merge_sort(self.lista_ordenada.copy())
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.5f} segundos.")
        inicio = time.time()
        Ordenacao.merge_sort(self.lista_desordenada.copy())
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.5f} segundos.\n")

    def test_performance_ordenacao_quick_sort(self):
        print("Teste de performance para ordenação com Quick Sort:\n")
        inicio = time.time()
        Ordenacao.quick_sort(self.lista_ordenada.copy())
        fim = time.time()
        print(f"Lista ordenada em: {fim - inicio:.5f} segundos.")
        inicio = time.time()
        Ordenacao.quick_sort(self.lista_desordenada.copy())
        fim = time.time()
        print(f"Lista desordenada em: {fim - inicio:.5f} segundos.")

    def run_tests(self):
        self.test_performance_busca_sequencial()
        self.test_performance_busca_binaria()
        self.test_performance_ordenacao_bubble_sort()
        self.test_performance_ordenacao_selection_sort()
        self.test_performance_ordenacao_insertion_sort()
        self.test_performance_ordenacao_merge_sort()
        self.test_performance_ordenacao_quick_sort()
        print("\nTodos os testes de performance foram executados.\n")

if __name__ == '__main__':
    testes = Performance()
    testes.run_tests()