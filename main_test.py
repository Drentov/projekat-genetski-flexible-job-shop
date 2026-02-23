from Chromosome import Chromosome
from Decoder import Decoder
from FJSPInstance import FJSPInstance
from GeneticAlgorithm import GeneticAlgorithm
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


    gen_alg= GeneticAlgorithm(instance,
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

    ga = GeneticAlgorithm(
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

    ga = GeneticAlgorithm(
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

def complex_test():
    instance_data = [

        # Job 0 (7 ops) -- bottleneck-heavy, long processing
        [
            [(0, 15), (1, 20), (3, 12)],
            [(2, 18), (4, 10), (6, 22)],
            [(1, 14), (5, 19)],
            [(0, 11), (3, 17), (7, 9)],
            [(2, 13), (4, 16), (6, 20)],
            [(1, 8),  (5, 12), (7, 15)],
            [(3, 10), (6, 14)]
        ],

        # Job 1 (6 ops)
        [
            [(1, 12), (2, 17), (5, 9)],
            [(0, 20), (4, 14)],
            [(3, 11), (6, 18), (7, 13)],
            [(1, 16), (2, 10)],
            [(4, 15), (5, 21), (7, 8)],
            [(0, 13), (3, 19)]
        ],

        # Job 2 (9 ops) -- longest job, stress-tests sequencing
        [
            [(0, 8),  (2, 12)],
            [(1, 15), (3, 10), (6, 18)],
            [(4, 11), (5, 16)],
            [(0, 13), (7, 9)],
            [(2, 20), (3, 14), (6, 11)],
            [(1, 9),  (4, 17)],
            [(5, 12), (7, 15)],
            [(0, 16), (3, 8),  (6, 13)],
            [(2, 11), (4, 19)]
        ],

        # Job 3 (5 ops) -- short but uses rare machines
        [
            [(6, 22), (7, 18)],
            [(5, 14), (6, 10)],
            [(3, 25), (7, 16)],
            [(4, 12), (6, 20)],
            [(5, 17), (7, 11)]
        ],

        # Job 4 (7 ops)
        [
            [(0, 14), (1, 9),  (4, 17)],
            [(2, 11), (3, 16)],
            [(1, 20), (5, 13), (7, 10)],
            [(0, 8),  (4, 15)],
            [(2, 18), (3, 12), (6, 9)],
            [(1, 13), (5, 22)],
            [(4, 10), (7, 16)]
        ],

        # Job 5 (8 ops) -- high machine overlap with Job 2, creates contention
        [
            [(0, 10), (2, 14)],
            [(1, 18), (3, 11)],
            [(4, 15), (6, 9)],
            [(0, 12), (5, 20), (7, 8)],
            [(2, 16), (3, 13)],
            [(1, 10), (4, 18)],
            [(5, 14), (6, 11)],
            [(0, 9),  (7, 17)]
        ],

        # Job 6 (6 ops)
        [
            [(3, 13), (5, 8),  (7, 16)],
            [(0, 19), (2, 14)],
            [(1, 11), (4, 17), (6, 10)],
            [(3, 15), (5, 12)],
            [(0, 8),  (2, 20), (7, 13)],
            [(4, 16), (6, 9)]
        ],

        # Job 7 (7 ops) -- spread across all machines
        [
            [(0, 11), (7, 14)],
            [(1, 16), (6, 10)],
            [(2, 13), (5, 18)],
            [(3, 9),  (4, 15)],
            [(1, 20), (7, 12)],
            [(0, 14), (6, 17)],
            [(2, 8),  (5, 11)]
        ],

        # Job 8 (5 ops) -- very tight times, easy to schedule
        [
            [(1, 7),  (2, 9),  (3, 5)],
            [(0, 8),  (4, 6)],
            [(5, 7),  (6, 10)],
            [(2, 5),  (7, 8)],
            [(3, 6),  (4, 9),  (6, 7)]
        ],

        # Job 9 (8 ops) -- long times, competes with Job 0 and Job 2
        [
            [(0, 18), (3, 14)],
            [(1, 22), (5, 16)],
            [(2, 12), (4, 20), (7, 15)],
            [(0, 10), (6, 18)],
            [(3, 13), (5, 9)],
            [(1, 17), (4, 11)],
            [(2, 15), (7, 22)],
            [(0, 12), (6, 16)]
        ],

        # Job 10 (6 ops)
        [
            [(4, 13), (5, 17)],
            [(0, 10), (2, 14), (6, 8)],
            [(1, 19), (3, 12)],
            [(4, 15), (7, 11)],
            [(2, 9),  (5, 16), (6, 13)],
            [(0, 14), (3, 18)]
        ],

        # Job 11 (7 ops) -- uses predominantly M0 and M1, creates local bottleneck
        [
            [(0, 16), (1, 12)],
            [(0, 14), (2, 18), (5, 11)],
            [(1, 20), (3, 15)],
            [(0, 9),  (4, 13)],
            [(1, 17), (6, 10)],
            [(0, 12), (5, 16)],
            [(1, 11), (7, 14)]
        ],

        # Job 12 (5 ops) -- all with 3 alternatives, very flexible
        [
            [(1, 10), (3, 13), (5, 16)],
            [(0, 14), (4, 11), (6, 18)],
            [(2, 12), (5, 9),  (7, 15)],
            [(1, 17), (3, 10), (6, 13)],
            [(0, 11), (4, 16), (7, 8)]
        ],

        # Job 13 (9 ops) -- second longest, extreme sequencing pressure
        [
            [(2, 14), (4, 10)],
            [(1, 16), (5, 12), (7, 20)],
            [(0, 11), (3, 18)],
            [(2, 15), (6, 9)],
            [(4, 13), (5, 17)],
            [(1, 8),  (7, 14)],
            [(0, 16), (3, 11), (6, 12)],
            [(2, 10), (4, 15)],
            [(5, 18), (7, 13)]
        ],

        # Job 14 (6 ops) -- moderate, balances the load
        [
            [(3, 12), (6, 16), (7, 10)],
            [(0, 18), (2, 13)],
            [(1, 11), (4, 15), (5, 9)],
            [(3, 14), (7, 17)],
            [(0, 10), (6, 12)],
            [(2, 16), (4, 8),  (5, 13)]
        ],
    ]

    instance = FJSPInstance(instance_data)

    ga = GeneticAlgorithm(
        instance,
        population_size=80,
        generations=200,
        mutation_rate=0.25,
        tournament_size=4,
        crossover_rate=0.85
    )

    best, best_hist, avg_hist = ga.run()

    print(f"FINAL BEST MAKESPAN: {best.makespan}")

    plot_convergence(best_hist, avg_hist)
    makespan, _, _, machine_sched = Decoder.decode(instance, best)
    plot_gantt(machine_sched, instance.num_machines, makespan)

if __name__ == "__main__":

    trivial_and_verbose_test()
    realistic_test()
    heavy_test()
    complex_test()