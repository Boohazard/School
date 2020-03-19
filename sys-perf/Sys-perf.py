import psutil

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


print("="*40, "CPU Info", "="*40)
print("Fysieke cores:", psutil.cpu_count(logical=False))
print("Totale cores:", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Huidige Frequency: {cpufreq.current:.2f}Mhz")
print(f"Totale CPU Gebruik: {psutil.cpu_percent(interval=.1, percpu=False)}%")

print("="*40, "Memory info", "="*40)
svmem = psutil.virtual_memory()
print(f"Totaal: {get_size(svmem.total)}")
print(f"Bruikbaar: {get_size(svmem.available)}")
print(f"Gebruikt: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")

print("="*40, "Schijf info", "="*40)
print("Partities en Gebruik:")
partitions = psutil.disk_partitions()
for partition in partitions:
    print("="*10, f"Schijf: {partition.device}", "="*10)
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f"  Totaal grootte: {get_size(partition_usage.total)}")
    print(f"  Gebruikt: {get_size(partition_usage.used)}")
    print(f"  Vrij: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
