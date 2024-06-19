# visuals.py

import matplotlib.pyplot as plt

def plot_schedule(schedule, algorithm_name):
    fig, ax = plt.subplots(figsize=(6, 4))
    
    process_names = [process['name'] for process in schedule]
    burst_times = [process['burst_time'] for process in schedule]
    
    ax.barh(process_names, burst_times, align='center')
    ax.set_xlabel('Burst Time')
    ax.set_title(f'{algorithm_name} Scheduling')
    
    return fig, ax
