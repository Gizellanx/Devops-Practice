# Day 7 – Linux Process Monitoring

## Objective

Learn how Linux manages running processes and practise monitoring system activity using terminal commands.

## Commands Practised

### Show Running Processes

```bash
ps aux
```

Displays all running processes, including CPU usage, memory usage, and process ownership.

### Search for Specific Processes

```bash
ps aux | grep python
ps aux | grep chrome
```

Used to filter and search for specific running processes.

### Real-Time System Monitoring

```bash
top
```

Displays live system activity, including:
- CPU usage
- Memory usage
- Active processes

Press:

```bash
q
```

to exit.

### Stop a Running Process

```bash
kill PID
```

Example:

```bash
kill 1234
```

Stops a process using its Process ID (PID).

### Force Stop a Process

```bash
kill -9 PID
```

Used when a process does not stop normally.

## Key Concepts

- Linux treats running applications as processes
- Processes consume CPU and memory resources
- Monitoring processes is important for troubleshooting and system performance
- Process investigation is a key part of Linux and DevOps workflows

## What I Learned

- How to inspect running processes
- How to monitor system activity in real time
- The difference between stopping a process normally and forcefully
- How Linux process monitoring supports troubleshooting workflows
