class FJSPInstance:
    """
    jobs structure:

    self.jobs[j][o] = list
    of(machine_id, processing_time)

        where:
        j = job index
        o = operation index within that job
    """

    def __init__(self, jobs : list[list[list[tuple]]]):

        self.jobs = jobs
        self.num_jobs = len(jobs)

        self.num_machines = self._infer_number_of_machines()
        self.total_operations = sum(len(job) for job in jobs)

    def _infer_number_of_machines(self): # Just finds maximum machine id and infers total machine count.

        max_machine_id = -1

        for job in self.jobs:
            for operation in job:
                for machine_id, _ in operation:
                    if machine_id > max_machine_id:
                        max_machine_id = machine_id

        return max_machine_id + 1

    def get_operation_options(self, job_id, operation_index): #Returns all possible machine options for a given operation.
        return self.jobs[job_id][operation_index]

    def get_processing_time(self, job_id, operation_index, machine_id): #Returns processing time for given job, operation, and machine.

        for machine_id, operation_time in self.jobs[job_id][operation_index]:
            if machine_id == machine_id:
                return operation_time

        raise ValueError("Machine not valid for this operation.")

    def operations_per_job(self):  #LIST containing an array of HOW MANY OPERATIONS each job has!
        return [len(job) for job in self.jobs]


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