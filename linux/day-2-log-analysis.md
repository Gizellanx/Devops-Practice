# Day 2 – Log File Analysis (Linux)

## Overview
In this task, I analysed a web server log file to identify the IP address that made the highest number of requests.

The log file contained one request per line, with the IP address in the first column.

## Objective
Find the IP address that appears most frequently in the log file and save it to a file.

## File Location
/home/admin/access.log

## Solution

```bash
awk '{print $1}' /home/admin/access.log | sort | uniq -c | sort -nr | head -1 | awk '{print $2}' > /home/admin/highestip.txt

Breakdown

    •    Extract IP addresses → awk '{print $1}'
    •    Sort data → sort
    •    Count occurrences → uniq -c
    •    Sort by highest count → sort -nr
    •    Get top result → head -1
    •    Extract IP → awk '{print $2}'
    •    Save output → > file

Key Concepts

    •    uniq only works on consecutive duplicates
    •    sort is required before counting
    •    Pipes (|) chain commands together
    •    Logs represent real system activity

Real-World Use

This type of analysis is used for:
    •    Monitoring server traffic
    •    Detecting suspicious behaviour (e.g. bots, attacks)
    •    Troubleshooting performance issues
    •    Identifying high-frequency users

Interview Questions

    •    How did you find the most frequent IP?
    •    Why is sorting required before using uniq?
    •    What does sort -nr do?
    •    What does awk do?
    •    What is the purpose of log analysis?

## Reflection

This task helped me understand how Linux commands can be combined to analyse log files. It also showed how important logs are in identifying system activity, such as detecting high traffic from a specific IP address.
