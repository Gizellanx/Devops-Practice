from collections import Counter

log_file = "../logs/access.log"

ip_addresses = []

with open(log_file, "r") as file:
    for line in file:
        ip = line.split()[0]
        ip_addresses.append(ip)

counter = Counter(ip_addresses)
most_common_ip, count = counter.most_common(1)[0]

print(f"Most active IP: {most_common_ip}")
print(f"Number of requests: {count}")
