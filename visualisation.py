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
