from process import Process

def srtf(processes):
    """Shortest Job First (Preemptive) - También conocido como SRTF (Shortest Remaining Time First)"""
    n = len(processes)
    completed = []
    current_time = 0
    completed_count = 0
    
    # Crear copias para no modificar los originales
    process_list = processes.copy()
    
    # Encontrar el tiempo máximo para la simulación
    max_time = max(p.arrival_time for p in process_list) + sum(p.burst_time for p in process_list)
    
    while completed_count < n:
        # Encontrar procesos disponibles
        available = [p for p in process_list if p.arrival_time <= current_time and p.remaining_time > 0]
        
        if not available:
            # Si no hay procesos disponibles, avanzar al siguiente arrival
            current_time += 1
            continue
        
        # Seleccionar el proceso con menor remaining_time
        current_process = min(available, key=lambda x: x.remaining_time)
        
        # Ejecutar por 1 unidad de tiempo
        current_process.remaining_time -= 1
        current_time += 1
        
        # Si el proceso terminó
        if current_process.remaining_time == 0:
            completed_count += 1
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed.append(current_process)
        
        # Prevenir bucles infinitos
        if current_time > max_time:
            break
    
    return completed
