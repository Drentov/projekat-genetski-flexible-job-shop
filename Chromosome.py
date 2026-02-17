import random

from FJSPInstance import FJSPInstance


class Chromosome:
    """
    Represents one individual solution in the genetic algorythm

    OS: Operation Sequence
    MS: Machine Selection (idx offset)
    """

    def __init__(self, os_sequence:list, ms_sequence:list):
        self.os = os_sequence #list of job id'd
        self.ms = ms_sequence #list of machine options offsets
        self.fitness = None
        self.makespan = None

    @staticmethod
    def random_initialize(instance:FJSPInstance): #creates a ramdom valid chromosome for the FJSP instance.

        os_sequence = [] #operation sequence initialiation

        operations_per_job = instance.operations_per_job()

        for job_id, operation_count in enumerate(operations_per_job):
            os_sequence += [job_id] * operation_count

        random.shuffle(os_sequence)

        ms_sequence = [] #machine selection sequence generation

        for job_id in range(instance.num_jobs):
            for op_index in range(len(instance.jobs[job_id])):
                options = instance.get_operation_options(job_id, op_index)
                chosen_options_index = random.randint(0, len(options) - 1)
                ms_sequence.append(chosen_options_index)

        return Chromosome(os_sequence, ms_sequence)