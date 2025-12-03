import sys
from process import Process
from process import read_csv, print_results
from fcfs import fcfs
from sjf import sjf
from priority_scheduling import priority_scheduling
from round_robin import round_robin
from srtf import srtf
from priority_pre import priority_preemptive

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python program.py input_file.csv [FCFS|SJF|PS|RR|SRTF|PP] [q=quantum]")
        sys.exit(1)
    
    filename = sys.argv[1]
    algorithm = sys.argv[2].upper()
    
    processes = read_csv(filename)
    
    print(f"\n{'='*84}")
    print(f"Algoritmo: {algorithm}")
    print(f"{'='*84}\n")
    
    if algorithm == "FCFS":
        result = fcfs(processes)
    elif algorithm == "SJF":
        result = sjf(processes)
    elif algorithm == "PS":
        result = priority_scheduling(processes)
    elif algorithm == "RR":
        if len(sys.argv) < 4:
            print("Error: Round Robin requiere el quantum time")
            print("Uso: python program.py input_file.csv RR q=quantum")
            sys.exit(1)
        quantum = int(sys.argv[3].split('=')[1])
        print(f"Quantum Time: {quantum} ms\n")
        result = round_robin(processes, quantum)
    elif algorithm == "SRTF":
        result = srtf(processes)
    elif algorithm == "PP":
        result = priority_preemptive(processes)
    else:
        print(f"Algoritmo desconocido: {algorithm}")
        print("Algoritmos válidos: FCFS, SJF, PS, RR, SRTF, PP")
        sys.exit(1)
    
    print_results(result)
    print()
    