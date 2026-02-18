import matplotlib.pyplot as plt

def plot_convergence(best_history, avg_history):
    plt.figure(figsize=(8, 5))
    plt.plot(best_history, label="Best Makespan")
    plt.plot(avg_history, label="Average Makespan")
    plt.xlabel("Generation")
    plt.ylabel("Makespan")
    plt.title("GA Convergence")
    plt.legend()
    plt.grid(True)
    plt.show()





def plot_gantt(machine_schedules, num_machines, makespan=None):

    #machine_schedules:
    #dict[machine_id] = list of (start, finish, job_id, operation_index)

    #num_machines:
    #total number of machines

    #makespan:
    #optional, just adds a vertical line

    fig, ax = plt.subplots(figsize=(14, 6))

    # Collects all job ids to assign consistent colors
    jobs = set()
    for ops in machine_schedules.values():
        for (_, _, job_id, _) in ops:
            jobs.add(job_id)

    jobs = sorted(jobs)
    colors = plt.cm.tab20(range(len(jobs)))
    job_color = {job: colors[i] for i, job in enumerate(jobs)}

    # Plot each machine row
    for machine_id in range(num_machines):

        for (start, finish, job_id, op_idx) in machine_schedules[machine_id]:

            duration = finish - start

            ax.barh(
                y=machine_id,
                width=duration,
                left=start,
                color=job_color[job_id],
                edgecolor='black'
            )

            # Label inside the bar
            ax.text(
                start + duration / 2,
                machine_id,
                f"J{job_id}-O{op_idx}",
                ha='center',
                va='center',
                fontsize=7
            )

    # draws makespan line, if provided
    if makespan is not None:
        ax.axvline(makespan, linestyle='--')

    ax.set_xlabel("Time")
    ax.set_ylabel("Machine")
    ax.set_yticks(range(num_machines))
    ax.set_yticklabels([f"M{i}" for i in range(num_machines)])
    ax.set_title("Flexible Job Shop Gantt Chart")
    ax.grid(True)

    plt.tight_layout()
    plt.show()
