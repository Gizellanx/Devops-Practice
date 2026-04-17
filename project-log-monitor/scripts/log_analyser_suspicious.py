from collections import Counter

log_file = "../logs/access_advanced.log"

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        ip = line.split()[0]
        status_code = line.split()[-1]

        if status_code.startswith("4") or status_code.startswith("5"):
            failed_ips.append(ip)

counter = Counter(failed_ips)

for ip, count in counter.items():
    if count > 5:
        print(f"{ip} → {count} failed requests")
