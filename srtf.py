from process import Process

def srtf(processes):
    """Shortest Remaining Time First (Preemptive SJF)"""
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    completed = []
    remaining = processes.copy()
    
    while remaining:
        # Procesos disponibles en el tiempo actual
        available = [p for p in remaining if p.arrival_time <= current_time]
        
        if not available:
            current_time = remaining[0].arrival_time
            continue
        
        # Seleccionar el proceso con menor remaining_time
        process = min(available, key=lambda x: x.remaining_time)
        
        # Ejecutar por 1 unidad de tiempo
        process.remaining_time -= 1
        current_time += 1
        
        # Si el proceso terminó
        if process.remaining_time == 0:
            remaining.remove(process)
            process.completion_time = current_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            completed.append(process)
    
    return completed