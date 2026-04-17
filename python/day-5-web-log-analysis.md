# Day 5 – Web Log Analysis (Python)

## Overview
Analysed web server logs to extract useful information such as active users, failed requests, and suspicious activity.

## Objectives
- Identify most active IP addresses  
- Detect failed requests (4xx, 5xx)  
- Identify suspicious IPs based on request thresholds  

## What I Practised
- Reading structured log files (access.log)  
- Extracting IP addresses and status codes  
- Using Python loops and conditions  
- Counting and filtering data  

## Key Scenarios

### Most Active IP
Extracted IP addresses, counted occurrences using Counter, and identified the IP with the highest number of requests.

```python
from collections import Counter

log_file = "../logs/access.log"

ip_addresses = []

with open(log_file, "r") as file:
    for line in file:
        ip = line.split()[0]
        ip_addresses.append(ip)

counter = Counter(ip_addresses)
most_common_ip, count = counter.most_common(1)[0]

print(f"Most active IP: {most_common_ip}")
print(f"Number of requests: {count}")
```

### Failed Requests
Extracted status codes and filtered for client and server errors (4xx and 5xx).

```python
failed_requests = 0

with open(log_file, "r") as file:
    for line in file:
        status_code = line.split()[-1]

        if status_code.startswith("4") or status_code.startswith("5"):
            failed_requests += 1

print(f"Total failed requests: {failed_requests}")
```

### Suspicious IP Detection
Counted failed requests per IP and flagged any IP exceeding a defined threshold.

```python
from collections import Counter

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        parts = line.split()
        ip = parts[0]
        status_code = parts[-1]

        if status_code.startswith("4") or status_code.startswith("5"):
            failed_ips.append(ip)

counter = Counter(failed_ips)

for ip, count in counter.items():
    if count > 5:
        print(f"{ip} -> {count} failed requests")
```

## Key Learning
The same Python structure can be reused across different scenarios, with only the logic changing depending on what data is being analysed. This reflects real DevOps work, where scripts are adapted for monitoring, troubleshooting, and security analysis.
