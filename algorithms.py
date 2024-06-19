# algorithms.py

import queue

def fcfs(processes):
    # FCFS scheduling
    schedule = []
    for process in processes:
        schedule.append(process)
    return schedule

def round_robin(processes, quantum):
    # Round Robin scheduling
    schedule = []
    ready_queue = queue.Queue()
    for process in processes:
        ready_queue.put(process)
    
    while not ready_queue.empty():
        process = ready_queue.get()
        if process['burst_time'] > quantum:
            process['burst_time'] -= quantum
            ready_queue.put(process)
        else:
            schedule.append(process)
    
    return schedule
