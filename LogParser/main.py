def check_username(file):
    failure_events = {}

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            timestamp = parts[0]
            user = parts[1]
            ip = parts[2]
            status = parts[3]

            if status == "FAIL":
                failure_events.setdefault(user, {"Failed logins": 0, "ips": [], "timestamps": []})
                failure_events[user]["Failed logins"] += 1
                failure_events[user]["ips"].append(ip)
                failure_events[user]["timestamps"].append(timestamp)

    for u, info in failure_events.items():
        print(f"{u} has failed {info['Failed logins']} times from {info['ips']} at {info['timestamps']}")


check_username("log.txt")