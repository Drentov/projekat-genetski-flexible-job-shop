class FJSPInstance:
    """
    jobs structure:

    self.jobs[j][o] = list
    of(machine_id, processing_time)

        where:
        j = job index
        o = operation index within that job
    """

    def __init__(self, jobs : list[
        list[ # of jobs
            list[ #of operations
                tuple #possible execution machines and their timing
            ]
        ]
    ]):

        self.jobs = jobs
        self.num_jobs = len(jobs)

        self.num_machines = self._infer_number_of_machines()
        self.total_operations = sum(len(job) for job in jobs)
        self.job_operation_offsets = self._compute_job_operation_offsets()

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

    def get_processing_time(self, job_id, operation_index, given_machine_id): #Returns processing time for given job, operation, and machine.

        for machine_id, operation_time in self.jobs[job_id][operation_index]:
            if machine_id == given_machine_id:
                return operation_time

        raise ValueError("Machine not valid for this operation.")

    def operations_per_job(self):  #LIST containing an array of HOW MANY OPERATIONS each job has!
        return [len(job) for job in self.jobs]

    def _compute_job_operation_offsets(self):

        offsets = []
        current_index = 0

        for job in self.jobs:
            offsets.append(current_index)
            current_index += len(job)

        return offsets # list where index j gives starting index of job j in Machine Selection array


    def get_ms_index(self, job_id, operation_index):
        return self.job_operation_offsets[job_id] + operation_index
