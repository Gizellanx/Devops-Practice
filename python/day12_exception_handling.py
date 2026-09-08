import os

log_file = "logs/access.log"

try:
    if not os.path.exists(log_file):
        raise FileNotFoundError(f"Log file not found: {log_file}")

    with open(log_file, "r") as file:
        lines = file.readlines()

    print("Log file opened successfully.")
    print(f"Total log entries: {len(lines)}")

except FileNotFoundError as error:
    print(f"ERROR: {error}")

except PermissionError:
    print("ERROR: Permission denied when trying to access the log file.")

except Exception as error:
    print(f"UNEXPECTED ERROR: {error}")
