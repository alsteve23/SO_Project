import csv


class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.priority = int(priority)
        self.remaining_time = int(burst_time)
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def read_csv(filename):
    """Lee el archivo CSV y retorna una lista de procesos"""
    processes = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            priority = int(row.get('priority', 0))
            process = Process(row['pid'], row['arrival_time'], row['burst_time'], priority)
            processes.append(process)
    return processes

def print_results(processes):
    """Imprime los resultados en formato tabla"""
    print(f"{'PID':<10}{'Arrival':<12}{'Burst':<10}{'Priority':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<12}")
    print("-" * 84)
    
    total_turnaround = 0
    total_waiting = 0
    
    for p in processes:
        print(f"{p.pid:<10}{p.arrival_time:<12}{p.burst_time:<10}{p.priority:<10}"
              f"{p.completion_time:<15}{p.turnaround_time:<15}{p.waiting_time:<12}")
        total_turnaround += p.turnaround_time
        total_waiting += p.waiting_time
    
    n = len(processes)
    print("-" * 84)
    print(f"\nAverage Turnaround Time: {total_turnaround/n:.2f} ms")
    print(f"Average Waiting Time: {total_waiting/n:.2f} ms")
