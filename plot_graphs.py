import matplotlib.pyplot as plt

f = open("time_values_basic.txt", "r")
time_tracker = f.readlines()
time_tracker = [float(i.strip()) for i in time_tracker]

f = open("time_values_efficient.txt", "r")
time_tracker_dnc = f.readlines()
time_tracker_dnc = [float(i.strip()) for i in time_tracker_dnc]

f = open("mem_values_basic.txt", "r")
memory_tracker = f.readlines()
memory_tracker = [float(i.strip()) for i in memory_tracker]

f = open("mem_values_efficient.txt", "r")
memory_tracker_dnc = f.readlines()
memory_tracker_dnc = [float(i.strip()) for i in memory_tracker_dnc]

xaxis = [
    16,
    64,
    128,
    256,
    384,
    512,
    768,
    1024,
    1280,
    1536,
    2048,
    2560,
    3072,
    3584,
    3968
]

def build_plots():
    # Generate Problem Size vs CPU
    plt.xlabel("Problem Size")
    plt.ylabel("CPU Time (milliseconds)")
    plt.title("Comparison of Sequence Alignment Implementations")
    plt.plot(xaxis, time_tracker, label="Basic")
    plt.plot(xaxis, time_tracker_dnc, label="Efficient")
    # plt.xticks(range(len(xaxis)), xaxis, rotation=45)
    plt.legend()
    plt.savefig('CPUPlot.png', format='png')
    plt.show()

    print()

    # Generate Problem Size vs Memory
    plt.xlabel("Problem Size")
    plt.ylabel("Memory Utilization (in kb)")
    plt.title("Comparison of Sequence Alignment Implementations")
    plt.plot(xaxis, memory_tracker, label="Basic")
    plt.plot(xaxis, memory_tracker_dnc, label="Efficient")
    plt.legend()
    plt.savefig('MemoryPlot.png', format='png')
    plt.show()


build_plots()
