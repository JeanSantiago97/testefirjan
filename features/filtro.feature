#Language: pt

Funcionalidade: Ordernar os resultados por A-Z, Z-A, Recentes e antigos

'''
    Como cliente, quero ordenar o resultado da busca por A-Z, Z-A, Mais recentes e Mais antigos.
'''

Contexto: Ao pesquisar algum item

Cenário: Ordenar os resultados de A-Z
Dado que abro o menu de ordenação A-Z
Quando seleciono a opção A-Z
Então devo visualizar os resultados de A-Z

Cenário: Ordenar os resultados de Z-A
Dado que abro o menu de ordenação Z-A
Quando seleciono a opção Z-A
Então devo visualizar os resultados de Z-A

Cenário: Ordenar os resultados por Mais recentes
Dado que abro o menu de ordenação Mais recentes
Quando seleciono a opção Mais recentes
Então devo visualizar os resultados por Mais recentes

Cenário: Ordenar os resultados por Mais antigos
Dado que abro o menu de ordenação Mais antigos
Quando seleciono a opção Mais antigos
Então devo visualizar os resultados por Mais antigos