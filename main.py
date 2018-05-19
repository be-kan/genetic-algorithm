from numpy.random import *


# 個体を表すクラス
class Individual():

    def __init__(self, gene_list):
        self.gene_list = gene_list
        self.fitness = sum(gene_list)  # 適応度

    # 二点交叉
    def crossover(self, individual):
        random_array = randint(0, 50, 2)
        for i in range(random_array.min(), random_array.max()):
            tmp = self.gene_list[i]
            self.gene_list[i] = individual.gene_list[i]
            individual.gene_list[i] = tmp

        new_individual = Individual(self.gene_list)
        new_individual_2 = Individual(individual.gene_list)

        return new_individual, new_individual_2

    # 突然変異（置換）
    def mutate(self):
        for i in range(len(self.gene_list)):
            random_num = randint(100)
            if random_num > 80:
                if self.gene_list[i] == 0:
                    self.gene_list[i] = 1
                else:
                    self.gene_list[i] = 0

        new_individual = Individual(self.gene_list)

        return new_individual


# 世代を表すクラス
class Generation:
    def __init__(self, N_gene, N_individual):
        self.n_gene = N_gene
        self.n_individual = N_individual
        self.individual_list = []

    # 第一世代を生成する
    def create_first_generation(self):
        for i in range(self.n_individual):
            gene_list = []
            for i in range(self.n_gene):
                gene_list.append(randint(2))

            self.individual_list.append(Individual(gene_list))

        return self

    # 次の世代を生成する
    def create_next_generation(self):
        # 40個体を交叉で生成する
        for i in range(0, 20):
            random_pair = randint(0, 40, 2)
            new_individual, new_individual_2 = self.individual_list[random_pair.min()].crossover(self.individual_list[random_pair.max()])
            self.individual_list.append(new_individual)
            self.individual_list.append(new_individual_2)

        # 10個体を突然変異で生成する
        for i in range(40, 50):
            mutated_individual = self.individual_list[i].mutate()
            self.individual_list.append(mutated_individual)

        # selectする
        individual_dict = {}
        for i in range(100):
            individual_dict[self.individual_list[i]] = self.individual_list[i].fitness

        individual_dict = sorted(individual_dict.items(), key=lambda x: x[1])
        print('MAX' + str(individual_dict[99][1]) + 'MIN' + str(individual_dict[0][1]))

        new_individual_list = []
        for i in range(100):
            new_individual_list.append(individual_dict[i][0])

        self.individual_list = new_individual_list[50:100]
        shuffle(self.individual_list)

        return self


def main():
    N_gene = 100  # 遺伝子数
    N_individual = 50  # 個体数

    generation = Generation(N_gene, N_individual).create_first_generation()
    for i in range(100):
        generation = generation.create_next_generation()


if __name__ == "__main__":
    main()
