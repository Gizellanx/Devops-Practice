from datetime import datetime

alert = f"""
===========================
DEVOPS ALERT
===========================

Time: {datetime.now()}

Status: WARNING

A monitoring check has detected an issue.

Please investigate:

- CPU
- Memory
- Disk
- API Availability

===========================
"""

with open("../output/alerts.txt", "w") as file:
    file.write(alert)

print("Alert generated successfully.")
