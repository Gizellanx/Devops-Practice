# Day 2 — Python Log Analyser

## Objective
Analyse a log file using Python and detect system issues such as errors and warnings.

## What I Did
- Opened and read a log file using Python
- Looped through each line in the file
- Checked for keywords like ERROR, WARNING, and INFO
- Used conditions (if, and, or) to filter specific issues
- Counted errors and warnings
- Printed results and a summary

## Key Logic
```python
error_count = 0
warning_count = 0

with open("server.log", "r") as file:
    for line in file:
        if ("cpu" in line or "disk" in line or "memory" in line) and "ERROR" in line:
            error_count += 1
            print("ISSUE FOUND:", line.strip())

        elif ("cpu" in line or "disk" in line or "memory" in line) and "WARNING" in line:
            warning_count += 1
            print("ISSUE FOUND:", line.strip())

print("\nSummary:")
print("Total Errors:", error_count)
print("Total Warnings:", warning_count)

Output

ISSUE FOUND: ERROR cpu overheating
ISSUE FOUND: WARNING disk space almost full

Summary:
Total Errors: 2
Total Warnings: 1

What I Learned
    •    How to read and process log files
    •    How to filter data using conditions
    •    The difference between and and or
    •    How to control script behaviour

Next
    •    Improve output structure
    •    Store results in lists
    •    Move to the next Python script
