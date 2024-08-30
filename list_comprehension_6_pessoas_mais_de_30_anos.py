"""
Dada uma lista de tuplas, onde cada tupla contém um nome e uma idade,
crie uma nova lista com apenas os nomes das pessoas que têm idade maior que 30.

pessoas = [("Maria", 28), ("João", 35), ("Ana", 42), ("Pedro", 22), ("Carla", 31)]

Requisito: Utilize list comprehension para gerar a nova lista com apenas os nomes.

Dica: Desestruture as tuplas na list comprehension para acessar a idade e o nome
separadamente.
"""

pessoas = [("Maria", 28), ("João", 35), ("Ana", 42), ("Pedro", 22), ("Carla", 31)]

mais_de_30 = [nome for nome, idade in pessoas if idade > 30]

print(mais_de_30)
