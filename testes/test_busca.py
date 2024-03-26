import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from algoritmos.busca import Busca
import random


class TesteBusca:
    def __init__(self) -> None:
        self.lista = [3, 5, 7, 9, 27, 34, 63, 88, 89]
        
    def test_busca_sequencial(self):
        valor = [random.randint(1, 100) for _ in range(5)]
        
        for v in valor:
            try:
                if Busca.busca_sequencial(self.lista, v) == self.lista.index(v):
                    print(f"Teste de busca sequencial ({v}) passou.")
            except:
                print(f"Teste de busca sequencial ({v}) falhou.")

    def test_busca_binaria(self):
        try:
            assert Busca.busca_binaria(self.lista, 34) == 5
            assert Busca.busca_binaria(self.lista, 88) == 3
            assert Busca.busca_binaria(self.lista, 27) == -1
            print("Teste de busca binária passou.")
        except AssertionError:
            print("Teste de busca binária falhou.")
            return

    def run_tests(self):
        self.test_busca_sequencial()
        self.test_busca_binaria()
        print("Fim dos testes.")

if __name__ == '__main__':
    testes = TesteBusca()
    testes.run_tests()  
