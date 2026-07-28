# Day 12 - Cron Jobs

## Objective

Learn how to schedule tasks automatically using cron, allowing scripts and commands to run at specified times without manual intervention.

## What I Practised

- Creating scheduled tasks with `crontab`
- Editing the user's cron table
- Understanding cron schedule syntax
- Listing existing cron jobs
- Removing scheduled cron jobs
- Scheduling scripts to run automatically

## Commands Used

```bash
crontab -e
crontab -l
crontab -r

* * * * * /path/to/script.sh
0 * * * * /path/to/script.sh
0 9 * * 1 /path/to/script.sh
```

## What I Learned

- Cron is a Linux service used to automate repetitive tasks.
- Scheduled jobs are stored in a user's crontab.
- Cron uses a five-field schedule to determine when commands should run.
- Automating tasks reduces manual work and improves consistency.

## Why This Matters

Automation is a core DevOps practice. Cron allows engineers to schedule monitoring scripts, backups, health checks, and maintenance tasks without requiring manual execution.
