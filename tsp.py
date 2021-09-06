""" Implémentation du problème de voyageur de commerce en utilisant l'AG. """

import random
import copy

""" Graphe de l'exemple:
        0 7 6 8 3
        7 0 2 4 3
        6 2 0 5 6
        8 4 5 0 4
        3 3 6 4 0
    """

def initPopulation(nb_individus, nb_gene):
    """ nb_individus: Nombre de solution à générer \n
        nb_gene : Nombre de gènes par individu: nb de sommets \n
    """
    population = []
    for cp in range(nb_individus):
        individu = []
        while len(individu)<nb_gene:
            val = random.randint(0, nb_gene-1)
            if val not in individu:
                individu.append(val)
        population.append(individu)
    return population

def crossover(ind1, ind2, pc):
    """ ind1, ind2 : sont deux individus \n
        pc : la probabilité de crossover 
    """
    ofs1 = copy.deepcopy(ind1)
    ofs2 = copy.deepcopy(ind2)
    nb = int(pc * len(ind1))
    offsp1 = ind1[:nb] + ofs2[nb:]
    offsp2 = ind2[:nb] + ofs1[nb:]
    return offsp1, offsp1

def correction(ind):
    n = len(ind)
    ind_correct = [-1]*n
    ind_ = [k for k in range(n)]
    for i in range(n):
        if ind[i] not in ind_correct:
            ind_correct[i] = ind[i]
            ind_.remove(ind[i])
    for j in range(n):
        if ind_correct[j] == -1:
            ind_correct[j] = ind_[0]
            ind_.remove(ind_[0])
    return ind_correct

def mutation(individu, pm):
    n = len(individu)
    nb = int(pm*n)
    for i in range(nb):
        i1 = random.randint(0, n-1)
        i2 = random.randint(0, n-1)
        individu[i1], individu[i2] = individu[i2], individu[i1]
    return individu

def poids_ind(ind):
    dist = 0
    n = len(ind)-1
    for i in range(n):
        dist += graphe[ind[i]][ind[i+1]]
    dist += graphe[ind[n]][ind[0]] # Chemin retour
    return dist

def fitnessFunction(population, graphe):
    """ Le graphe ici est donné par la matrice des poids """
    pop_size = len(population)
    fitnessValues = []
    for ind in population:
        dist = 0
        n = len(ind)-1
        for i in range(n):
            dist += graphe[ind[i]][ind[i+1]]
        dist += graphe[ind[n]][ind[0]] # Chemin retour
        fitnessValues.append([ind, dist])
    return fitnessValues

def unique(liste):
    set_list = []
    for elt in liste:
        if elt not in set_list:
            set_list.append(elt)
    return set_list

def selection_rang(fitnessValues):
    select = copy.deepcopy(fitnessValues)
    nwlists = unique(select)
    nwlist = sorted(nwlists, key=lambda x: x[1])
    return nwlist[0][0], nwlist[0][0]

def selection(fitnessValues):
    select = copy.deepcopy(fitnessValues)
    nwlist = sorted(select, key=lambda x: x[1])
    return nwlist[0]

graphe = [  [0, 7, 6, 8, 3], 
            [7, 0, 2, 4, 3], 
            [6, 2, 0, 5, 6], 
            [8, 4, 5, 0, 4], 
            [3, 3, 6, 4, 0]
        ]


def main():
    pop_size      = 6
    pc            = 0.75
    pm            = 0.1
    nb_generation = 5
    population    = initPopulation(pop_size, 5)
    i  = 0 
    while i < nb_generation:
        nvlle_gen     = []
        fitnessValues = fitnessFunction(population, graphe)
        for j in range(6):
            s1, s2 = selection_rang(fitnessValues)
            o1, o2 = crossover(s1, s2, pc)
            o11 = mutation(o1, pm)
            o22 = mutation(o2, pm)
            o11 = correction(o11)
            o22 = correction(o22)
            nvlle_gen.append(o11)
            nvlle_gen.append(o22)
        population = copy.deepcopy(nvlle_gen)
        i = i+1
    return selection(fitnessValues)
    # i1, i2, i3, i4, i5 = selectionner_cinq(population, fitnessValues)
    # return (i1, poids_ind(i1)), (i2, poids_ind(i2)), (i3, poids_ind(i3)), (i4, poids_ind(i4)), (i5, poids_ind(i5))

solution = main()
print(solution)

