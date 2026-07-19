import subprocess
import os

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

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(["python", os.path.join(current_directory, script)])

print("\nAll monitoring tasks completed.")
