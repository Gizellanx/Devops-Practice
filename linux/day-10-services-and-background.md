# Day 12 – Linux Services & Background Processes

## Objective

Learn how Linux manages services and background processes that keep systems running.

## What I Practised

Today I explored how Linux services run in the background and how administrators monitor them.

I practised checking service status, viewing running processes, and understanding how system services support applications and servers.

## Commands Used

```bash
systemctl status ssh
systemctl list-units --type=service
ps aux
ps aux | grep ssh
top
```

## What I Learned

- How Linux services run in the background
- How to check whether a service is running correctly
- The difference between services and regular processes
- How process monitoring helps with troubleshooting
- Why service management is important for system reliability

## Why This Matters

DevOps engineers regularly monitor services to ensure applications remain available and healthy.

Understanding how services operate helps with troubleshooting, system administration, and maintaining reliable environments.
