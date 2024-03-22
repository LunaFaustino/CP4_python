from testes import test_ordenacao
from testes import test_busca


dicionario = test_ordenacao.listas()
for i in dicionario:
    test_ordenacao.teste_vetor(dicionario[i])

numero = int(input("\nDigite o número a ser pesquisado: "))
chave = input("""\nEm qual lista você deseja buscar:\n 
        lista_ordenado_crescente
        lista_nao_ordenado
        lista_ordenado_decrescente
        lista_vazio
        lista_unico_elemento
        lista_elementos_repetidos
        lista_aleatoria10
        lista_aleatoria100
        lista_aleatoria1000""")

if chave in dicionario:
    resultado = test_busca.busca_numero(dicionario[chave], numero)
else:
    print("Chave inválida.")









