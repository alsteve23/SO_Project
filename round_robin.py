from process import Process


def round_robin(processes, quantum,overhead=1):
    """Round Robin"""
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    queue = []
    remaining = processes.copy()
    completed = []
    previous_process = None
    context = 0

    # Agregar el primer proceso disponible
    if remaining:
        queue.append(remaining.pop(0))

    while queue or remaining:

        if not queue:
            # Si no hay procesos en cola, avanzar al siguiente arrival
            current_time = remaining[0].arrival_time
            queue.append(remaining.pop(0))
            previous_process = None

        process = queue.pop(0)

        # Aplicar overhead si hay cambio de contexto
        if (
            overhead > 0
            and previous_process is not None
            
        ):

            context += 1
            current_time += overhead
            print(process.pid)
            print(context)

        # Ejecutar por quantum o hasta completar
        execution_time = min(quantum, process.remaining_time)
        current_time += execution_time

        process.remaining_time -= execution_time

        # Agregar procesos que llegaron durante la ejecución
        arrived = [p for p in remaining if p.arrival_time <= current_time]
        for p in arrived:
            queue.append(p)
            remaining.remove(p)

        # Si el proceso terminó
        if process.remaining_time == 0:
            process.completion_time = current_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            completed.append(process)
            previous_process = None
        else:
            # Regresar a la cola
            queue.append(process)
            previous_process = process


    return completed
