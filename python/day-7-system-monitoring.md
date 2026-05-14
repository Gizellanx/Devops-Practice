# Day 7 – Python System Monitoring

## Objective

Learn how Python can be used to monitor basic system resources such as CPU, memory, and disk usage.

## What I Worked On

Today I started learning how system monitoring works in Python. The goal was to understand how monitoring scripts can check system resources automatically instead of manually inspecting the system through the terminal.

This also helped connect the Linux process monitoring work from the previous session with Python automation.

## CPU Monitoring

```python
import psutil

cpu_usage = psutil.cpu_percent()

print(f"CPU Usage: {cpu_usage}%")
```

This checks the current CPU usage of the system.

## Memory Monitoring

```python
import psutil

memory = psutil.virtual_memory()

print(f"Memory Usage: {memory.percent}%")
```

This displays the current memory usage.

## Disk Monitoring

```python
import psutil

disk = psutil.disk_usage('/')

print(f"Disk Usage: {disk.percent}%")
```

This checks how much disk space is currently being used.

## Basic Alert Logic

```python
import psutil

cpu_usage = psutil.cpu_percent()

if cpu_usage > 80:
    print("High CPU usage detected")
else:
    print("CPU usage is normal")
```

This introduces simple monitoring alerts using conditions.

## What I Learned

- How Python can be used for basic system monitoring
- The connection between Linux monitoring and Python automation
- How monitoring scripts can help identify system issues
- How conditions can be used to trigger alerts

## Next Steps

- Combine CPU, memory, and disk monitoring into one script
- Improve output formatting
- Continue building monitoring and automation skills
