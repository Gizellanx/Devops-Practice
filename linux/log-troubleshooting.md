# Linux Troubleshooting: Log File Issue

## Scenario
A program was continuously writing to a log file:

/var/log/bad.log

This caused the log file to grow and consume disk space.

---

## Objective
Identify the process writing to the log file and stop it without deleting the file.

---

## Step 1: Observe the Log Activity

### Command:
tail -f /var/log/bad.log

### Purpose:
- Monitor log file in real time
- Confirm continuous writing

---

## Step 2: Identify the Process

### Command:
lsof /var/log/bad.log

### Purpose:
- Find which process is using the file

### Result:
- Process: badlog.py
- PID: 593

---

## Step 3: Stop the Process

### Command:
sudo kill 593

### Purpose:
- Terminate the process causing the issue

---

## Step 4: Verify the Fix

### Command:
tail -f /var/log/bad.log

### Result:
- No new log entries
- Issue resolved

---

## Key Concepts Learned
- Log monitoring using `tail -f`
- Identifying processes with `lsof`
- Stopping processes using `kill`
- Basic Linux troubleshooting workflow

---

## DevOps Relevance
This reflects real-world scenarios where:
- Logs grow uncontrollably
- Systems run out of disk space
- Engineers must diagnose and fix issues quickly

Typical workflow:
1. Observe the problem
2. Investigate logs
3. Identify root cause
4. Fix the issue
5. Verify the solution
