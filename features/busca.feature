#Language: pt

Funcionalidade: Realizar pesquisa na página principal

'''
    Como cliente, quero fazer uma pesquisa na página da firjan.
'''
Contexto: Acessar a página de teste
Dado que acesso o site da Firjan

Cenário: acessar a página principal da firjan e fazer uma pesquisa
Dado que pesquiso pela palavra Firjan
Quando clico no botão pesquisar
Então devo visualizar os resultados
