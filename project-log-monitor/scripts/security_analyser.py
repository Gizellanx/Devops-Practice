from collections import Counter

log_file = "../logs/security.log"
output_file = "../output/security_report.txt"

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        if "FAILED LOGIN" in line:
            ip = line.split()[-1]
            failed_ips.append(ip)

counter = Counter(failed_ips)

with open(output_file, "w") as report:
    report.write("Security Report\n")
    report.write("=================\n\n")

    for ip, count in counter.items():
        report.write(f"{ip} -> {count} failed logins\n")

print("Security report generated.")
