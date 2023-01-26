import mlrose_hiive as mlr

pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'
voos = {}

for linha in open('./files/flights.txt'):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

agenda = [1, 2, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]


def fitness(agenda_voos):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda_voos) // 2):
        origem_voo = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem_voo, destino)][agenda_voos[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem_voo)][agenda_voos[id_voo]]
        total_preco += volta[2]

    return total_preco


def imprimir_voos(agenda_voo):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda_voo) // 2):
        nome = pessoas[i][0]
        origem_voo = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem_voo, destino)][agenda_voo[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem_voo)][agenda_voo[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s'
              % (nome, origem_voo, ida[0], ida[1], ida[2], volta[0], volta[1], volta[2]))
    print('Preço total: ', total_preco)


ft = mlr.CustomFitness(fitness)
problema = mlr.DiscreteOpt(12, ft, False, 10)

melhor_solucao, melhor_custo, state = mlr.hill_climb(problema, random_state=1)


melhor_solucao_annealing, melhor_custo_annealing, state_annealing = mlr.simulated_annealing(
    problema,
    schedule=mlr.GeomDecay(init_temp=10000),
    random_state=1
)

melhor_solucao_genetic, melhor_custo_genetic, state_genetic = mlr.genetic_alg(
    problema,
    pop_size=500,
    mutation_prob=0.2,
    random_state=1
)

imprimir_voos(melhor_solucao_genetic)

