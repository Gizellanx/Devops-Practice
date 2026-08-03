import subprocess
import os
from datetime import datetime

print("=" * 40)
print("Project Log Monitor")
print("=" * 40)

scripts = [
    "log_analyser.py",
    "security_analyser.py",
    "system_monitor.py",
    "api_monitor.py",
    "deployment_health.py"
]

current_directory = os.path.dirname(__file__)

# Create monitoring summary
summary_file = os.path.join(current_directory, "..", "output", "monitoring_summary.txt")

with open(summary_file, "w") as summary:
    summary.write("=" * 40 + "\n")
    summary.write("PROJECT LOG MONITOR SUMMARY\n")
    summary.write("=" * 40 + "\n\n")
    summary.write(f"Run Date: {datetime.now()}\n\n")

    for script in scripts:
        print(f"Running {script}...")
        subprocess.run(["python", os.path.join(current_directory, script)])

        summary.write(f"{script:<30} COMPLETED\n")

    summary.write("\nOverall Status: SUCCESS\n")
    summary.write("=" * 40)

print("\nMonitoring completed successfully.")
