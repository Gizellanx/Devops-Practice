# Day 9 – Process Management & Background Jobs

## Objective

Learn how Linux manages running processes and how to run, stop, and control tasks from the terminal.


## What I Worked On

Today I learned how Linux handles processes running in the foreground and background.

I practised viewing active jobs, sending tasks to the background, bringing them back to the foreground, and understanding how processes continue running while other work is being performed.

## Running a Process in the Background

```bash
sleep 300 &
```

The ampersand (`&`) sends the process to the background, allowing the terminal to be used for other commands.

## Viewing Background Jobs

```bash
jobs
```

Displays processes currently running in the background.

## Bringing a Job Back to the Foreground

```bash
fg
```

Moves a background job back into the active terminal session.

## Sending a Job to the Background

```bash
bg
```

Continues a stopped process in the background.

## Running a Process After Closing the Terminal

```bash
nohup command &
```

Example:

```bash
nohup python3 script.py &
```

This allows a process to continue running even after the terminal session is closed.

## What I Learned

- The difference between foreground and background processes
- How to manage running jobs from the terminal
- How Linux allows multiple tasks to run at the same time
- Why long-running processes are often sent to the background

## Key Takeaway

Process management is important because many Linux systems run multiple services and tasks at the same time. Understanding how to control those processes helps with troubleshooting and system administration.
