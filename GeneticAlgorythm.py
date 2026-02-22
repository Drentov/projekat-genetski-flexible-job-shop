import random
from Decoder import Decoder
from Chromosome import Chromosome



class GeneticAlgorythm:

    def __init__(self,
            instance,
            population_size=30,
            generations=100,
            mutation_rate=0.2,
            crossover_rate=0.8,
            tournament_size=3):

        self.instance = instance
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size

        self.population = []
        self.best_individual = None
        self.best_history = [] #to track best makespan per generation
        self.avg_history = [] #to track average makespan per generation


    def initialize_population(self):
        self.population = [
            Chromosome.random_initialize(self.instance)
            for _ in range(self.population_size)
        ]

    def evaluate_population(self):

        for individual in self.population:
            if individual.fitness is None:
                Decoder.decode(self.instance, individual)

    def tournament_selection(self):
        participants = random.sample(self.population, self.tournament_size)
        return max(participants, key=lambda individual: individual.fitness)

    def mutate(self, chromosome:Chromosome):

        # Swap mutation for OS
        # Random machine reassignment for MS

        #OS mutation
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(chromosome.os)), 2)
            chromosome.os[i], chromosome.os[j] = chromosome.os[j], chromosome.os[i] #apparently this is fine in python!

        #MS mutation
        if random.random() < self.mutation_rate:
            ms_index = random.randint(0, len(chromosome.ms) - 1)

            #identify job + operation for this MS index

            for job_id in range(self.instance.num_jobs):
                start = self.instance.job_operation_offsets[job_id]
                end = start + len(self.instance.jobs[job_id])

                if start <= ms_index < end: #to avoid mutating it to an invalid MS index!
                    operations_index = ms_index - start
                    options = self.instance.get_operation_options(job_id, operations_index)

                    chromosome.ms[ms_index] = random.randint(0, len(options) - 1)
                    break


        chromosome.fitness = None #also, we invalidate these after mutation!
        chromosome.makespan = None


    def crossover_os(self, parent1, parent2): #Going here with: Precedence Operation Crossover (POX) (basically  sublists in order combination)

        size = len(parent1.os)

        #random select subset of jobs
        job_ids = list(range(self.instance.num_jobs))
        num_selected = random.randint(1, self.instance.num_jobs - 1)
        selected_jobs = set(random.sample(job_ids, num_selected))

        #initilaise child
        child_os = [None] * size

        #copy selected jobs from parent1
        for i in range(size):
            if parent1.os[i] in selected_jobs:
                child_os[i] = parent1.os[i]


        #fill remaining positions from parent2
        parent2_pointer = 0

        for i in range(size):
            if child_os[i] is None:

                #just move ptr till we find job not selected
                while parent2.os[parent2_pointer] in selected_jobs:
                    parent2_pointer += 1

                child_os[i] = parent2.os[parent2_pointer]
                parent2_pointer +=1

        return  child_os


    def crossover_ms(self, parent1, parent2): #Going here with: a simple uniform crossover

        child_ms = []

        for i in range (len(parent1.ms)):
            if random.random() < 0.5:
                child_ms.append(parent1.ms[i])
            else:
                child_ms.append(parent2.ms[i])


        return child_ms


    def run(self):

        self.initialize_population()
        self.evaluate_population()

        for generation in range(self.generations):

            #best first (reverse) sort
            self.population.sort(key=lambda individual: individual.fitness, reverse=True)

            #a bit of performance tracking...
            best_makespan = self.population[0].makespan
            avg_makespan = sum(individual.makespan for individual in self.population) / len(self.population)

            self.best_history.append(best_makespan)
            self.avg_history.append(avg_makespan)

            #keep best
            new_population = [self.population[0]]

            #if necessary, update best individual
            if self.best_individual is None or (self.population[0].fitness > self.best_individual.fitness):
                self.best_individual = self.population[0] #if new iteration elite is better than current best!


            #re-generate rest
            while len(new_population) < self.population_size:

                parent1 = self.tournament_selection()
                parent2 = self.tournament_selection()

                if random.random() < self.crossover_rate:
                    child_os = self.crossover_os(parent1, parent2)
                    child_ms = self.crossover_ms(parent1, parent2)
                else:
                    child_os = parent1.os.copy()
                    child_ms = parent1.ms.copy()

                child = Chromosome(child_os, child_ms)

                self.mutate(child) #a bit of random mutation

                new_population.append(child)


            self.population = new_population
            self.evaluate_population()

            if generation % 10 == 0:
                print(f"Generation {generation}, Best makespan: {self.population[0].makespan}")

        return self.best_individual, self.best_history, self.avg_history













