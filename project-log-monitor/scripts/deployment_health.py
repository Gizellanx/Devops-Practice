import json
import psutil
import requests

with open("config.json", "r") as file:
    config = json.load(file)

cpu_threshold = config["cpu_threshold"]
memory_threshold = config["memory_threshold"]
disk_threshold = config["disk_threshold"]
api_url = config["api_url"]

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

try:
    response = requests.get(api_url, timeout=5)
    api_status = "PASS" if response.status_code == 200 else "FAIL"
except requests.exceptions.RequestException:
    api_status = "FAIL"

print("Deployment Health Check")
print("-----------------------")
print(f"CPU: {cpu}%")
print(f"Memory: {memory}%")
print(f"Disk: {disk}%")
print(f"API: {api_status}")

if (
    cpu < cpu_threshold
    and memory < memory_threshold
    and disk < disk_threshold
    and api_status == "PASS"
):
    print("Deployment Successful")
else:
    print("Deployment Requires Investigation")
