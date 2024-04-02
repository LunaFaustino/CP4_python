from algoritmos.busca import Busca
from algoritmos.ordenacao import Ordenacao
import time

class Performance:
    def __init__(self):
        self.lista_ordenada_100 = [i for i in range(100)]
        self.lista_ordenada_1000 = [i for i in range(1000)]
        self.lista_ordenada_10000 = [i for i in range(10000)]
        self.lista_ordenada_10000.sort()
        self.lista_desordenada_100 = [i for i in range(100)]
        self.lista_desordenada_1000 = [i for i in range(1000)]
        self.lista_desordenada_10000 = [i for i in range(10000)]
        self.lista_desordenada_10000.reverse()

    def test_performance_busca_sequencial(self):
        print("\nTeste de performance para busca sequencial:\n")
        self._test_performance_busca_sequencial(self.lista_ordenada_100, "Lista ordenada 100")
        self._test_performance_busca_sequencial(self.lista_ordenada_1000, "Lista ordenada 1000")
        self._test_performance_busca_sequencial(self.lista_ordenada_10000, "Lista ordenada 10000")
        self._test_performance_busca_sequencial(self.lista_desordenada_100, "Lista desordenada 100")
        self._test_performance_busca_sequencial(self.lista_desordenada_1000, "Lista desordenada 1000")
        self._test_performance_busca_sequencial(self.lista_desordenada_10000, "Lista desordenada 10000")

    def _test_performance_busca_sequencial(self, lista, nome_lista):
        inicio = time.time()
        Busca.busca_sequencial(lista, lista[-1])
        fim = time.time()
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_busca_binaria(self):
        print("\nTeste de performance para busca binária:\n")
        self._test_performance_busca_binaria(self.lista_ordenada_100, "Lista ordenada 100")
        self._test_performance_busca_binaria(self.lista_ordenada_1000, "Lista ordenada 1000")
        self._test_performance_busca_binaria(self.lista_ordenada_10000, "Lista ordenada 10000")
        self._test_performance_busca_binaria(self.lista_desordenada_100, "Lista desordenada 100")
        self._test_performance_busca_binaria(self.lista_desordenada_1000, "Lista desordenada 1000")
        self._test_performance_busca_binaria(self.lista_desordenada_10000, "Lista desordenada 10000")

    def _test_performance_busca_binaria(self, lista, nome_lista):
        inicio = time.time()
        Busca.busca_binaria(lista, lista[-1])
        fim = time.time()
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_bubble_sort(self):
        print("\nTeste de performance para ordenação com Bubble Sort:\n")
        self._test_performance_ordenacao_bubble_sort(self.lista_ordenada_100, "Lista ordenada 100")
        self._test_performance_ordenacao_bubble_sort(self.lista_ordenada_1000, "Lista ordenada 1000")
        self._test_performance_ordenacao_bubble_sort(self.lista_ordenada_10000, "Lista ordenada 10000")
        self._test_performance_ordenacao_bubble_sort(self.lista_desordenada_100, "Lista desordenada 100")
        self._test_performance_ordenacao_bubble_sort(self.lista_desordenada_1000, "Lista desordenada 1000")
        self._test_performance_ordenacao_bubble_sort(self.lista_desordenada_10000, "Lista desordenada 10000")

    def _test_performance_ordenacao_bubble_sort(self, lista, nome_lista):
        inicio = time.time()
        Ordenacao.bubble_sort(lista.copy())
        fim = time.time()
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_selection_sort(self):
        print("\nTeste de performance para ordenação com Selection Sort:\n")
        self._test_performance_ordenacao_selection_sort(self.lista_ordenada_100, "Lista ordenada 100")
        self._test_performance_ordenacao_selection_sort(self.lista_ordenada_1000, "Lista ordenada 1000")
        self._test_performance_ordenacao_selection_sort(self.lista_ordenada_10000, "Lista ordenada 10000")
        self._test_performance_ordenacao_selection_sort(self.lista_desordenada_100, "Lista desordenada 100")
        self._test_performance_ordenacao_selection_sort(self.lista_desordenada_1000, "Lista desordenada 1000")
        self._test_performance_ordenacao_selection_sort(self.lista_desordenada_10000, "Lista desordenada 10000")

    def _test_performance_ordenacao_selection_sort(self, lista, nome_lista):
        inicio = time.time()
        Ordenacao.selection_sort(lista.copy())
        fim = time.time()
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_insertion_sort(self):
        print("\nTeste de performance para ordenação com Insertion Sort:\n")
        self._test_performance_ordenacao_insertion_sort(self.lista_ordenada_100, "Lista ordenada 100")
        self._test_performance_ordenacao_insertion_sort(self.lista_ordenada_1000, "Lista ordenada 1000")
        self._test_performance_ordenacao_insertion_sort(self.lista_ordenada_10000, "Lista ordenada 10000")
        self._test_performance_ordenacao_insertion_sort(self.lista_desordenada_100, "Lista desordenada 100")
        self._test_performance_ordenacao_insertion_sort(self.lista_desordenada_1000, "Lista desordenada 1000")
        self._test_performance_ordenacao_insertion_sort(self.lista_desordenada_10000, "Lista desordenada 10000")

    def _test_performance_ordenacao_insertion_sort(self, lista, nome_lista):
        inicio = time.time()
        Ordenacao.insertion_sort(lista.copy())
        fim = time.time()
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_merge_sort(self):
        print("\nTeste de performance para ordenação com Merge Sort:\n")
        self._test_performance_ordenacao_merge_sort(self.lista_ordenada_100, "Lista ordenada 100")
        self._test_performance_ordenacao_merge_sort(self.lista_ordenada_1000, "Lista ordenada 1000")
        self._test_performance_ordenacao_merge_sort(self.lista_ordenada_10000, "Lista ordenada 10000")
        self._test_performance_ordenacao_merge_sort(self.lista_desordenada_100, "Lista desordenada 100")
        self._test_performance_ordenacao_merge_sort(self.lista_desordenada_1000, "Lista desordenada 1000")
        self._test_performance_ordenacao_merge_sort(self.lista_desordenada_10000, "Lista desordenada 10000")

    def _test_performance_ordenacao_merge_sort(self, lista, nome_lista):
        inicio = time.time()
        Ordenacao.merge_sort(lista.copy())
        fim = time.time()
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_quick_sort(self):
        print("\nTeste de performance para ordenação com Quick Sort:\n")
        self._test_performance_ordenacao_quick_sort(self.lista_ordenada_100, "Lista ordenada 100")
        self._test_performance_ordenacao_quick_sort(self.lista_ordenada_1000, "Lista ordenada 1000")
        self._test_performance_ordenacao_quick_sort(self.lista_ordenada_10000, "Lista ordenada 10000")
        self._test_performance_ordenacao_quick_sort(self.lista_desordenada_100, "Lista desordenada 100")
        self._test_performance_ordenacao_quick_sort(self.lista_desordenada_1000, "Lista desordenada 1000")
        self._test_performance_ordenacao_quick_sort(self.lista_desordenada_10000, "Lista desordenada 10000")

    def _test_performance_ordenacao_quick_sort(self, lista, nome_lista):
        inicio = time.time()
        Ordenacao.quick_sort(lista.copy())
        fim = time.time()
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

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
