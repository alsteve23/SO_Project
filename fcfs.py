def fcfs(processes):
    """First Come First Serve"""
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time = process.completion_time
    
    return processes