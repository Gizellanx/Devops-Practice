# Day 11 – Shell Scripting for Automation

## Objective

Learn how Bash scripts can automate common Linux tasks, reducing manual work and improving consistency.

## What I Did

- Created a simple Bash script to automate system checks
- Displayed the current date and time
- Checked disk usage
- Checked memory usage
- Identified the current logged-in user
- Saved the results into a report file

## Commands Used

```bash
#!/bin/bash

echo "System Report"
echo "-------------"

date
whoami
df -h
free -h
```

Run the script:

```bash
chmod +x system_report.sh
./system_report.sh
```

## Example Output

```text
System Report
-------------

Mon Jul 27 10:45:12 BST 2026

corlene

Filesystem      Size  Used Avail Use%
/dev/sda1       100G   45G   50G   48%

               total        used        free
Mem:            15Gi       6.2Gi       7.8Gi
```

## What I Learned

- How Bash scripts automate repetitive Linux tasks
- How multiple Linux commands can be combined into one script
- Why automation improves efficiency and consistency
- How shell scripting supports everyday DevOps work

## Next Improvements

- Save reports automatically with timestamps
- Monitor CPU usage
- Add error handling
- Schedule the script using cron jobs

## Why This Matters

Automation is a core DevOps principle. Instead of running several commands manually, engineers create shell scripts to perform routine checks quickly and consistently. This saves time, reduces human error, and makes systems easier to manage.
