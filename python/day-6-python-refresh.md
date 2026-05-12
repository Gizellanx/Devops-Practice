# Day 6 – Python Refresh & Log Investigation

## Objective

Reconnect with previous Python log analysis projects by reviewing scripts, revisiting Linux log investigation commands, and improving overall understanding of monitoring workflows.

## What I Practised

### Linux Log Investigation

Used Linux commands to search and inspect log data.

#### Commands Used

```bash
grep "ERROR" access.log
grep "404" access.log
tail access.log
cat access.log
```

### Python Log Analysis Refresh

Reviewed existing Python scripts used for analysing web server logs and suspicious activity.

#### Areas Reviewed
- Reading log files
- Extracting IP addresses
- Filtering failed requests
- Using loops and conditions
- Counting suspicious activity
- Structured script output

## Script Improvement Example

```python
from collections import Counter

log_file = "../logs/access.log"

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        parts = line.split()

        ip = parts[0]
        status_code = parts[-1]

        if status_code.startswith("4") or status_code.startswith("5"):
            failed_ips.append(ip)

counter = Counter(failed_ips)

print("\nSuspicious IP Report\n")

for ip, count in counter.items():
    if count > 5:
        print(f"IP Address: {ip}")
        print(f"Failed Requests: {count}")
        print("----------------------")
```

## Key Learning

- Refreshed Python file handling and filtering logic
- Revisited Linux troubleshooting workflows
- Improved understanding of log-based monitoring
- Continued rebuilding consistency with GitHub practice

## Next Steps

- Improve script output formatting
- Continue Linux command-line revision
- Build confidence with Python scripting
- Expand monitoring and automation practice
