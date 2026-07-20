# Day 11 - Python Logging

## Objective

Learn how to use Python's built-in `logging` module to record application events instead of relying on `print()` statements.

## What I Did

- Imported Python's `logging` module
- Configured a log file using `logging.basicConfig()`
- Recorded informational messages
- Recorded warning messages
- Recorded error messages
- Generated a log file containing application events

## Key Logic

```python
import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Monitoring started")
logging.warning("CPU usage exceeded threshold")
logging.error("API health check failed")
```

## Example Output

```
2026-07-20 10:15:42 - INFO - Monitoring started
2026-07-20 10:15:43 - WARNING - CPU usage exceeded threshold
2026-07-20 10:15:44 - ERROR - API health check failed
```

## What I Learned

- Python provides a built-in logging system for recording application events.
- Different log levels help categorise informational messages, warnings and errors.
- Writing logs to a file makes troubleshooting easier than relying on terminal output.

## Next Improvements

- Rotate log files automatically.
- Record monitoring results from multiple scripts.
- Store logs in a dedicated logs directory.

## Key Takeaway

Using Python's logging module creates a permanent record of application activity, making it easier to monitor systems and troubleshoot issues.
