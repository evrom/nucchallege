import subprocess

# cpupower -c all frequency-set -u 800mhz
# cpupower -c all frequency-set -u 2700mhz
cmd_cpu_high = ['sudo', 'cpupower',
                '-c', 'all', 'frequency-set', '-u', '2700mhz']
cmd_cpu_low = ['sudo', 'cpupower',
               '-c', 'all', 'frequency-set', '-u', '800mhz']


def cpu_high():
    subprocess.call(cmd_cpu_high)


def cpu_low():
    subprocess.call(cmd_cpu_low)
