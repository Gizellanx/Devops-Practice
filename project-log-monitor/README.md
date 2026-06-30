# Log Monitoring Tool

This project is a simple monitoring tool built using Python and Linux concepts to simulate tasks commonly performed by DevOps engineers.

## Overview

The project analyses log files, monitors system health, checks API availability, and generates reports to help identify potential issues before they affect a system.

## Project Structure

- logs → sample log files used for analysis
- scripts → Python monitoring and analysis scripts
- output → generated monitoring reports

## Current Features

- Log analysis for web server activity
- Security log analysis for failed login attempts
- System monitoring (CPU, memory and disk usage)
- API health monitoring
- Deployment health validation
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

If all checks pass, the deployment is considered healthy. If any check fails or exceeds a defined threshold, the report highlights that further investigation is required.

## How It Works

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

## What I Practised

- Python automation
- Log analysis
- System monitoring
- API monitoring
- Security monitoring
- Report generation
- Combining multiple monitoring tasks into a single DevOps workflow

## Why This Matters

Monitoring is a core responsibility in DevOps. Rather than manually checking different systems, monitoring tools automate health checks, identify potential problems, and provide useful reports that help engineers respond quickly to incidents.

## Future Improvements

- Combine all monitoring scripts into a single workflow
- Store monitoring history
- Add configurable alert thresholds
- Send notifications when critical issues are detected
- Support monitoring multiple services and APIs
