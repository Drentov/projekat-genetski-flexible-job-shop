from Chromosome import Chromosome
from Decoder import Decoder
from FJSPInstance import FJSPInstance

if __name__ == "__main__":

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


    chromosome = Chromosome.random_initialize(instance)

    makespan, start_times, finish_times, machine_sched = Decoder.decode(instance, chromosome)

    print("OS:", chromosome.os)
    print("MS:", chromosome.ms)
    print("Makespan:", makespan)
    print("Machine schedules:", machine_sched)