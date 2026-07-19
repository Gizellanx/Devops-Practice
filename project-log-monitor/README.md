# Log Monitoring Tool

This project is a simple monitoring tool built using Python and Linux concepts to simulate tasks commonly performed by DevOps engineers.

## Overview

The project analyses log files, monitors system health, checks API availability, and generates reports to help identify potential issues before they affect a system. Configuration settings are stored separately from the application code, making the tool easier to maintain and update.

## Project Structure

- logs → sample log files used for analysis
- scripts → Python monitoring and analysis scripts
- output → generated monitoring reports
- config.json → monitoring configuration settings

## Current Features

- Log analysis for web server activity
- Security log analysis for failed login attempts
- System monitoring (CPU, memory and disk usage)
- API health monitoring
- Deployment health validation
- Configuration management using `config.json`
- Unified monitoring runner using `run_monitor.py`
- Automated report generation

## Unified Monitoring Runner

### Objective

Improve the project by providing a single entry point that executes all monitoring tasks.

### What Was Added

- Created `run_monitor.py`
- Used Python's `subprocess` module to execute each monitoring script
- Centralised the monitoring workflow into a single command
- Prepared the project for future automation and scheduled monitoring

### Why This Matters

As monitoring applications grow, running individual scripts manually becomes inefficient. A unified monitoring runner allows every monitoring task to be started from a single command, making the application easier to use, maintain, and automate.

## Deployment Health Check

### Objective

Simulate the checks a DevOps engineer might perform after deploying an application.

### What It Checks

- CPU utilisation
- Memory utilisation
- Disk usage
- API availability
- Failed login activity

The monitoring thresholds and API endpoint are loaded from `config.json`, allowing the application's behaviour to be changed without modifying the source code.

If all checks pass, the deployment is considered healthy. If any check fails or exceeds a configured threshold, the report highlights that further investigation is required.

## How It Works

- Reads monitoring settings from `config.json`
- Executes all monitoring scripts through `run_monitor.py`
- Reads log files
- Monitors system resources
- Checks API availability
- Analyses security events
- Produces monitoring reports

## Example Outputs

- report.txt
- security_report.txt
- system_report.txt
- deployment_report.txt
- config_report.txt

## What I Practised

- Python automation
- Log analysis
- System monitoring
- API monitoring
- Security monitoring
- Configuration management
- Using Python's `subprocess` module
- Organising multiple monitoring scripts into a single workflow
- Report generation

## Why This Matters

Monitoring is a core responsibility in DevOps. Separating configuration from application code and providing a unified monitoring runner makes monitoring tools easier to maintain, automate, and extend as projects grow.

## Future Improvements

- Generate a monitoring summary report
- Store monitoring history
- Send notifications when critical issues are detected
- Schedule automated monitoring runs
- Support monitoring multiple services and APIs
