# main.py

import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt  # Import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from algorithms import fcfs, round_robin
from visuals import plot_schedule

class OSVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Visualization Tool")
        
        # Process data
        self.processes = [
            {'name': 'P1', 'burst_time': 10},
            {'name': 'P2', 'burst_time': 5},
            {'name': 'P3', 'burst_time': 8},
            {'name': 'P4', 'burst_time': 3},
            {'name': 'P5', 'burst_time': 12}
        ]
        
        # Labels
        ttk.Label(self.root, text="Select Scheduling Algorithm:").pack(pady=10)
        
        # Combo box for algorithms
        self.algorithm_var = tk.StringVar()
        algorithms = ['FCFS', 'Round Robin']
        self.algorithm_var.set(algorithms[0])
        ttk.OptionMenu(self.root, self.algorithm_var, *algorithms).pack()
        
        # Run button
        ttk.Button(self.root, text="Run", command=self.run_algorithm).pack(pady=10)
        
        # Matplotlib figure for visualization
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.chart_canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.chart_canvas.get_tk_widget().pack()

    def run_algorithm(self):
        algorithm = self.algorithm_var.get()
        
        if algorithm == 'FCFS':
            schedule = fcfs(self.processes)
        elif algorithm == 'Round Robin':
            quantum = 5  # Example quantum time
            schedule = round_robin(self.processes, quantum)
        else:
            messagebox.showerror("Error", "Unknown algorithm")
            return
        
        # Plotting using visuals.py
        self.figure, self.ax = plot_schedule(schedule, algorithm)
        self.chart_canvas.figure = self.figure
        self.chart_canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = OSVisualizationApp(root)
    root.mainloop()
