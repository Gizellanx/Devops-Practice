import psutil
import requests

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

try:
    response = requests.get("https://api.github.com", timeout=5)
    api_status = "PASS" if response.status_code == 200 else "FAIL"
except requests.exceptions.RequestException:
    api_status = "FAIL"

print("Deployment Health Check")
print("-----------------------")
print(f"CPU: {cpu}%")
print(f"Memory: {memory}%")
print(f"Disk: {disk}%")
print(f"API: {api_status}")

if cpu < 80 and memory < 80 and disk < 90 and api_status == "PASS":
    print("Deployment Successful")
else:
    print("Deployment Requires Investigation")
