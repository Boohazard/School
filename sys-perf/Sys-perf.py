import psutil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


print("="*40, "CPU Info", "="*40)
print("Fysieke cores:", psutil.cpu_count(logical=False))
print("Totale cores:", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
print(f"Max Frequentie: {cpufreq.max:.2f}Mhz")
print(f"Huidige Frequentie: {cpufreq.current:.2f}Mhz")
print(f"Totale CPU Gebruik: {psutil.cpu_percent(interval=.1, percpu=False)}%")

print("="*40, "Memory info", "="*40)
memory = psutil.virtual_memory()
print(f"Totaal: {get_size(memory.total)}")
print(f"Bruikbaar: {get_size(memory.available)}")
print(f"Gebruikt: {get_size(memory.used)}")
print(f"Percentage: {memory.percent}%")

print("="*40, "Schijf info", "="*40)
print("Partities en Gebruik:")
schijf = psutil.disk_partitions()
for schijf in schijf:
    print("="*10, f"Schijf: {schijf.device}", "="*10)
    print(f"  File system type: {schijf.fstype}")
    try:
        schijf_gebruik = psutil.disk_usage(schijf.mountpoint)
    except PermissionError:
        continue
    print(f"  Totaal grootte: {get_size(schijf_gebruik.total)}")
    print(f"  Gebruikt: {get_size(schijf_gebruik.used)}")
    print(f"  Vrij: {get_size(schijf_gebruik.free)}")
    print(f"  Percentage: {schijf_gebruik.percent}%")
