import re
import psutil


def cpu_usage():
    return psutil.cpu_percent(interval=0.1, percpu=True)


def cpu_frequency():
    hand = open('/proc/cpuinfo')
    frequencies = []
    for line in hand:
        line = line.rstrip()
        if re.search("cpu MHz", line):
            frequency_backwards = ''
            for character in reversed(line):
                if character == ' ':
                    break
                frequency_backwards += character
            frequencies.append(
                float(
                    frequency_backwards[::-1]
                    )
                )
    return frequencies

if __name__ == "__main__":
    print("CPU FREQUENCIES (MHz)")
    print(cpu_frequency())
    print("CPU USAGE (PERCENT)")
    print(cpu_usage())
