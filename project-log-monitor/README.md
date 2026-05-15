# Log Monitoring Tool

This project is a simple log analysis tool built using Python and the terminal to simulate how DevOps engineers work with system data.

## Overview

The script reads a log file, extracts IP addresses, and identifies the most active IP. The result is shown in the terminal and saved into a report file.

## Project Structure

- logs → contains the log file  
- scripts → contains the Python script  
- output → where the report is generated  

## How It Works

- The script reads the log file line by line  
- It extracts the IP address from each line  
- It counts how many times each IP appears  
- It finds the most active IP  
- It prints the result and saves it into a report  

## What I Practised

- Working with file structures (logs, scripts, output)  
- Reading and processing data using Python  
- Understanding reusable logic (same script, different scenarios)  
- Running scripts through the terminal instead of an IDE  
- Seeing how terminal interacts directly with system files  

## How to Run

cd project-log-monitor/scripts  
python3 log_analyser.py  

## Example Output

Most active IP: 10.0.0.5  
Number of requests: 5  
Report saved successfully  

## Why This Matters

This project helped me understand how log analysis can be automated. Instead of manually checking files, scripts can process data and generate useful results, which is a key part of DevOps workflows.

## Refresh Update

### Review Focus
- Revisited log analysis workflows using Python
- Reviewed failed request detection and IP extraction logic
- Re-analysed access logs and output generation
- Improved understanding of reusable monitoring scripts

### Current Improvements
- Reviewing existing script structure
- Cleaning project documentation
- Preparing for additional monitoring scenarios

## Day 8 – System Monitoring Automation

The project was expanded to include basic system monitoring using Python and psutil.

A new monitoring script was added to:
- check CPU usage
- check memory usage
- check disk usage
- generate monitoring reports automatically

The monitoring workflow now includes:
- scripts for automation
- logs for monitoring activity
- output reports for generated results

This helped connect Linux monitoring concepts with Python automation in a more practical workflow.
