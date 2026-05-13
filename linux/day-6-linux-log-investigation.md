# Day 6 – Linux Log Investigation Refresh

## Objective

Refresh Linux command-line workflows by revisiting log investigation commands and practising terminal-based troubleshooting techniques.

## Commands Practised

### View Log Files

```bash
cat access.log
tail access.log
```

### Search Log Data

```bash
grep "ERROR" access.log
grep "404" access.log
grep "WARNING" access.log
```

## What I Practised

- Viewing and reading log files through the terminal
- Searching logs for specific keywords and status codes
- Understanding how Linux commands assist with troubleshooting
- Revisiting command-line workflows used in DevOps environments


## Key Concepts

- Linux commands allow fast investigation of system and web server logs
- grep is used to filter specific data from log files
- tail is useful for viewing the most recent log entries
- Terminal-based troubleshooting is a core DevOps skill


## Example Workflow

```bash
grep "404" access.log
tail access.log
```

This workflow helps identify failed requests and inspect recent log activity directly from the terminal.


## Next Steps

- Continue Linux command-line revision
- Improve speed and confidence using terminal commands
- Combine Linux investigation with Python automation workflows
