import psutil

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("/").percent

print("System Monitoring Report")
print("------------------------")
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Disk Usage: {disk_usage}%")

with open("../output/system_report.txt", "w") as report:
    report.write("System Monitoring Report\n")
    report.write("------------------------\n")
    report.write(f"CPU Usage: {cpu_usage}%\n")
    report.write(f"Memory Usage: {memory_usage}%\n")
    report.write(f"Disk Usage: {disk_usage}%\n")

print("\nReport saved successfully.")
