# Python (DevOps Focus)

This folder contains Python scripts used for real-world DevOps-style tasks such as log analysis, monitoring, and automation.

## Focus
- Automating operational tasks  
- Processing and analysing log files  
- Extracting and filtering structured data  
- Building simple monitoring and detection tools  

## Scripts

### Day 2 – Log File Analyser (System Logs)
- Reads a log file line by line  
- Detects errors and warnings  
- Filters specific issues (CPU, disk, memory)  
- Counts and summarises results  

### Day 5 – Web Log Analysis (Access Logs)
- Extracts IP addresses from logs  
- Identifies most active users  
- Detects failed requests (4xx, 5xx)  
- Flags suspicious IPs based on thresholds  

## Skills Practised
- File handling (`open`, `read`)  
- Loops (`for`)  
- Conditions (`if`, `elif`)  
- Logical operators (`and`, `or`)  
- String processing (`split`, `startswith`)  
- Data counting using `collections.Counter`  

## Key Learning
The same script structure can be reused across multiple scenarios.  
Only the logic changes depending on what is being analysed (IPs, errors, requests, etc).

This reflects real DevOps work, where scripts are adapted for monitoring, troubleshooting, and security analysis.
