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
- Automated report generation

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
- Report generation
- Combining multiple monitoring tasks into a single DevOps workflow

## Why This Matters

Monitoring is a core responsibility in DevOps. Separating configuration from application code makes monitoring tools easier to maintain, more flexible, and simpler to adapt for different environments without changing the source code.

## Future Improvements

- Combine all monitoring scripts into a single workflow
- Store monitoring history
- Send notifications when critical issues are detected
- Schedule automated monitoring runs
- Support monitoring multiple services and APIs
