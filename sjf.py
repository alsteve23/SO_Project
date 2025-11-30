def sjf(processes):
    """Shortest Job First (Non-preemptive)"""
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    completed = []
    remaining = processes.copy()
    
    while remaining:
        # Procesos disponibles en el tiempo actual
        available = [p for p in remaining if p.arrival_time <= current_time]
        
        if not available:
            current_time = remaining[0].arrival_time
            continue
        
        # Seleccionar el proceso con menor burst_time
        process = min(available, key=lambda x: x.burst_time)
        remaining.remove(process)
        
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time = process.completion_time
        completed.append(process)
    
    return completed
