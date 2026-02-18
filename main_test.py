from Chromosome import Chromosome
from Decoder import Decoder
from FJSPInstance import FJSPInstance
from GeneticAlgorythm import GeneticAlgorythm
from visualisation import plot_convergence, plot_gantt


def trivial_and_verbose_test():

    jobs_example = [
        [  # Job 0
            [(0, 3), (1, 2)],      # Operation 0 (M0, 3H), (M1, 2H), aka operation 1 can take pace on: (machine 0, would take 3 hours) OR on: (machine 1, would take 2 hours)
            [(1, 4), (2, 5)]       # Operation 1
        ],
        [  # Job 1
            [(0, 2), (2, 3)],      # Operation 0
            [(1, 6)]               # Operation 1
        ]
    ]

    instance = FJSPInstance(jobs_example)

    print("Number of jobs:", instance.num_jobs)
    print("Number of machines:", instance.num_machines)
    print("Total operations:", instance.total_operations)
    print("Operations per job:", instance.operations_per_job())

    #"operacije jednog posla se moraju redom izvrsavati!"

    print("Offsets:", instance.job_operation_offsets)
    print("MS index of Job 1, Op 0:",
          instance.get_ms_index(1, 0))


    random_chromosome = Chromosome.random_initialize(instance)

    makespan, start_times, finish_times, machine_sched = Decoder.decode(instance, random_chromosome)

    print("OS:", random_chromosome.os)
    print("MS:", random_chromosome.ms)
    print("Makespan:", makespan)
    print("Machine schedules:", machine_sched)


    gen_alg= GeneticAlgorythm(instance,
                          population_size=30,
                          generations=50,
                          crossover_rate=0.8,
                          mutation_rate=0.3)

    best, best_hist, avg_hist  = gen_alg.run()

    print("\nFINAL BEST MAKESPAN:", best.makespan)

    plot_convergence(best_hist, avg_hist)
    makespan, _, _, machine_sched = Decoder.decode(instance, best)
    plot_gantt(machine_sched, instance.num_machines, makespan)

def realistic_test():
    jobs = [
        [
            [(0, 3), (1, 2), (2, 4)],
            [(0, 2), (2, 3)],
            [(1, 4), (2, 2)]
        ],
        [
            [(0, 2), (1, 1)],
            [(1, 3), (2, 4)],
            [(0, 4), (2, 3)]
        ],
        [
            [(1, 4), (2, 3)],
            [(0, 3), (2, 2)],
            [(0, 2), (1, 5)]
        ]
    ]

    instance = FJSPInstance(jobs)

    ga = GeneticAlgorythm(
        instance,
        population_size=50,
        generations=100,
        mutation_rate=0.2,
        tournament_size=3,
        crossover_rate=0.8
    )

    best, best_hist, avg_hist = ga.run()

    print("\nFINAL BEST MAKESPAN:", best.makespan)

    plot_convergence(best_hist, avg_hist)

    makespan, _, _, machine_sched = Decoder.decode(instance, best)
    plot_gantt(machine_sched, instance.num_machines, makespan)

def heavy_test():
    # 10 jobs, 6 machines
    instance_data = [
        # Job 0 (6 ops)
        [
            [(0, 12), (1, 8), (2, 15)],
            [(2, 10), (3, 18)],
            [(1, 14), (4, 9), (5, 20)],
            [(0, 7), (3, 16)],
            [(2, 11), (4, 13)],
            [(1, 9), (5, 17)]
        ],

        # Job 1 (5 ops)
        [
            [(1, 11), (2, 14)],
            [(0, 13), (3, 9), (4, 16)],
            [(2, 8), (5, 19)],
            [(1, 17), (3, 12)],
            [(0, 10), (4, 15)]
        ],

        # Job 2 (7 ops)
        [
            [(2, 9), (4, 14)],
            [(1, 13), (5, 11)],
            [(0, 16), (3, 10)],
            [(2, 7), (4, 12)],
            [(1, 15), (5, 18)],
            [(3, 9), (0, 14)],
            [(2, 11), (4, 13)]
        ],

        # Job 3 (6 ops)
        [
            [(0, 14), (1, 10), (5, 18)],
            [(2, 9), (3, 13)],
            [(4, 12), (1, 16)],
            [(0, 8), (2, 15)],
            [(3, 11), (5, 17)],
            [(1, 10), (4, 14)]
        ],

        # Job 4 (5 ops)
        [
            [(3, 12), (5, 9)],
            [(0, 15), (2, 10)],
            [(1, 13), (4, 8)],
            [(2, 16), (3, 11)],
            [(0, 14), (5, 12)]
        ],

        # Job 5 (6 ops)
        [
            [(1, 9), (4, 14)],
            [(2, 13), (5, 10)],
            [(0, 17), (3, 12)],
            [(1, 11), (4, 15)],
            [(2, 8), (5, 19)],
            [(3, 10), (0, 16)]
        ],

        # Job 6 (7 ops)
        [
            [(2, 14), (3, 9)],
            [(1, 10), (5, 13)],
            [(0, 18), (4, 11)],
            [(2, 7), (3, 15)],
            [(1, 12), (5, 16)],
            [(0, 14), (4, 10)],
            [(2, 9), (3, 13)]
        ],

        # Job 7 (6 ops)
        [
            [(4, 10), (5, 15)],
            [(0, 12), (1, 9)],
            [(2, 14), (3, 11)],
            [(1, 16), (4, 8)],
            [(0, 13), (5, 17)],
            [(2, 10), (3, 12)]
        ],

        # Job 8 (5 ops)
        [
            [(3, 9), (5, 14)],
            [(1, 15), (2, 10)],
            [(0, 16), (4, 12)],
            [(2, 11), (3, 18)],
            [(1, 13), (5, 9)]
        ],

        # Job 9 (6 ops)
        [
            [(0, 15), (2, 9)],
            [(1, 14), (4, 11)],
            [(3, 10), (5, 17)],
            [(2, 8), (0, 16)],
            [(4, 13), (1, 12)],
            [(3, 11), (5, 15)]
        ],
    ]

    instance = FJSPInstance(instance_data)

    ga = GeneticAlgorythm(
        instance,
        population_size=50,
        generations=100,
        mutation_rate=0.2,
        tournament_size=3,
        crossover_rate=0.8
    )

    best, best_hist, avg_hist = ga.run()

    print("\nFINAL BEST MAKESPAN:", best.makespan)

    plot_convergence(best_hist, avg_hist)
    makespan, _, _, machine_sched = Decoder.decode(instance, best)
    plot_gantt(machine_sched, instance.num_machines, makespan)



if __name__ == "__main__":

    trivial_and_verbose_test()
    realistic_test()
    heavy_test()
