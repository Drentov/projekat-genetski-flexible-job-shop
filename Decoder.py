from FJSPInstance import FJSPInstance
from Chromosome import Chromosome

class Decoder: #Decodes a chromosome into an actual schedule and computes max finish time (aka makespan)!

    @staticmethod
    def decode(instance:FJSPInstance, chromosome:Chromosome):

        """
        Returns:
            makespan,
            operation_start_times,
            operation_finish_times,
            machine_schedules
        """

        num_jobs = instance.num_jobs
        num_machines = instance.num_machines

        #Tracking avaliability times
        machine_available_time = [0] * num_machines
        job_available_time = [0] * num_jobs

        #tracking also which operation of each job we are scheduling next
        job_next_operation = [0] * num_jobs

        #Storing also operation timing results
        # (job_id, operation_index) becomes: start / finish
        operation_start_times = {}
        operation_finish_times = {}

        #Machine schedule storage
        # machine_id becomes: list of (start, finish, job_id, operation_index)
        machine_schedules = { machine_idx: [] for machine_idx in range(num_machines) } #machine_idx: [] is a key-value pair


        #DECODING LOOP

        for job_id in chromosome.os:

            operation_index = job_next_operation[job_id]
            ms_index = instance.get_ms_index(job_id, operation_index)
            machine_option_index = chromosome.ms[ms_index]

            #actual Machine ID + processing time
            op_options = instance.get_operation_options(job_id, operation_index)
            machine_id, processing_time = op_options[machine_option_index]

            #start time
            start_time = max(machine_available_time[machine_id], job_available_time[job_id])

            finish_time = start_time + processing_time

            #updating availability
            machine_available_time[machine_id] = finish_time
            job_available_time[job_id] = finish_time

            #storing the timing
            operation_start_times[(job_id, operation_index)] = start_time
            operation_finish_times[(job_id, operation_index)] = finish_time

            machine_schedules[machine_id].append(
                (start_time, finish_time, job_id, operation_index)
            )

            #move to next operation of this job
            job_next_operation[job_id] += 1

        makespan = max(operation_finish_times.values())

        chromosome.makespan = makespan
        chromosome.fitness = 1 / makespan #since we are looking for smallest finish time!

        return makespan, operation_start_times, operation_finish_times, machine_schedules

