from algoritmos.busca import Busca
from algoritmos.ordenacao import Ordenacao
import time
import matplotlib.pyplot

class Performance:   
    def __init__(self):
        self.tempos = {}
        self.nome_listas = ["Lista ordenada 100", "Lista ordenada 1000", "Lista ordenada 10000", "Lista desordenada 100", "Lista desordenada 1000", "Lista desordenada 10000"]
        self.lista_ordenada_100 = [i for i in range(100)]
        self.lista_ordenada_1000 = [i for i in range(1000)]
        self.lista_ordenada_10000 = [i for i in range(10000)]
        self.lista_ordenada_100.sort()
        self.lista_ordenada_1000.sort()
        self.lista_ordenada_10000.sort()
        self.lista_desordenada_100 = [i for i in range(100)]
        self.lista_desordenada_1000 = [i for i in range(1000)]
        self.lista_desordenada_10000 = [i for i in range(10000)]
        self.lista_desordenada_100.reverse()
        self.lista_desordenada_1000.reverse()
        self.lista_desordenada_10000.reverse()

    def test_performance_busca_sequencial(self):
        print("\nTeste de performance para busca sequencial:\n")
        self.tempos["busca_sequencial"] = []
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
        self.tempos["busca_sequencial"].append((fim - inicio))
        print(f"{nome_lista} em: {fim - inicio:.7f} segundos.")
        

    def test_performance_busca_binaria(self):
        print("\nTeste de performance para busca binária:\n")
        self.tempos["busca_binaria"] = []
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
        self.tempos["busca_binaria"].append(fim - inicio)
        print(f"{nome_lista} em: {fim - inicio:.7f} segundos.")

    def test_performance_ordenacao_bubble_sort(self):
        print("\nTeste de performance para ordenação com Bubble Sort:\n")
        self.tempos["buble_sort"] = []
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
        self.tempos["buble_sort"].append(fim - inicio)
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_selection_sort(self):
        print("\nTeste de performance para ordenação com Selection Sort:\n")
        self.tempos["selection_sort"] = []
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
        self.tempos["selection_sort"].append(fim - inicio)
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_insertion_sort(self):
        print("\nTeste de performance para ordenação com Insertion Sort:\n")
        self.tempos["insertion_sort"] = []
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
        self.tempos["insertion_sort"].append(fim - inicio)
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_merge_sort(self):
        print("\nTeste de performance para ordenação com Merge Sort:\n")
        self.tempos["merge_sort"] = []
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
        self.tempos["merge_sort"].append(fim - inicio)
        print(f"{nome_lista} em: {fim - inicio:.5f} segundos.")

    def test_performance_ordenacao_quick_sort(self):
        print("\nTeste de performance para ordenação com Quick Sort:\n")
        self.tempos["quick_sort"] = []
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
        self.tempos["quick_sort"].append(fim - inicio)
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


        tamanhos = self.nome_listas
        valores_busca_sequencial = self.tempos["busca_sequencial"]
        valores_busca_binaria = self.tempos["busca_binaria"]
        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(tamanhos,valores_busca_sequencial,'r',valores_busca_binaria,'b')
        matplotlib.pyplot.show()


        valores_buble_sort = self.tempos["buble_sort"]
        valores_selection_sort = self.tempos["selection_sort"]
        valores_insertion_sort = self.tempos["insertion_sort"]
        valores_merge_sort = self.tempos["merge_sort"]
        valores_quick_sort = self.tempos["quick_sort"]
        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(tamanhos,valores_buble_sort,'r',valores_selection_sort,'b',valores_insertion_sort,'y',valores_merge_sort,'g',valores_quick_sort,'p')
        matplotlib.pyplot.show()

if __name__ == '__main__':
    testes = Performance()
    testes.run_tests()
