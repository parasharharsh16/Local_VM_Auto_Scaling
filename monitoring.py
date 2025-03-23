import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

cpu_data = []
memory_data = []
time_data = []

def monitor_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent

    time_data.append(time.time())
    cpu_data.append(cpu_usage)
    memory_data.append(mem_usage)

    if len(time_data) > 50:
        time_data.pop(0)
        cpu_data.pop(0)
        memory_data.pop(0)

    print(f"CPU Usage: {cpu_usage}%, Memory Usage: {mem_usage}%")
    return cpu_usage, mem_usage

def update_plot(frame):
    plt.cla()
    plt.plot(time_data, cpu_data, label="CPU Usage (%)", color='r')
    plt.plot(time_data, memory_data, label="Memory Usage (%)", color='b')

    plt.ylim(0, 100)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Usage (%)')
    plt.legend(loc="upper right")
    plt.title('Real-Time CPU and Memory Usage')

if __name__ == "__main__":
    fig = plt.figure()
    
    ani = FuncAnimation(fig, update_plot, interval=1000) #to update the plot every 1 second

    try:
        while True:
            monitor_resources()
            plt.pause(1)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
