log_path = input("Enter the log file path: ")

with open(log_path, 'r') as file:
        lines = file.readlines()

        print(f"Total lines in log file: {len(lines)}")
        failed = 0
        for line in lines:
            if "failed" in line.lower():
                failed += 1

                print("failed logins", failed)

        success = 0
        for line in lines:
            if "success" in line.lower():
                success += 1

                print("successful logins", success)

        failed_ips ={}
        ip = line.split()[0]
        failed_ips[ip] = failed_ips.get(ip, 0) + 1