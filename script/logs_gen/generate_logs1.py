import random
import datetime


def generate_apple_logs(filename, num_lines=1000):
    events = ["CHECK_IN", "UPDATE_START", "CONFIG_PUSH", "HEARTBEAT"]
    devices = [f"MAC-{random.randint(100, 999)}",
               f"IPH-{random.randint(100, 999)}", f"IPD-{random.randint(100, 999)}"]
    statuses = ["SUCCESS", "ERROR"]
    error_codes = ["503", "401", "404", "500"]

    start_time = datetime.datetime(2026, 3, 17, 10, 0, 0)

    with open(filename, "w") as f:
        for i in range(num_lines):
            # Increment time by random seconds to simulate real traffic
            timestamp = (start_time + datetime.timedelta(seconds=i *
                         random.randint(1, 5))).strftime("%Y-%m-%dT%H:%M:%SZ")
            event = random.choice(events)
            device = random.choice(devices)
            status = random.choice(statuses)

            log_line = f'timestamp="{timestamp}" event="{event}" device_id="{device}" status="{status}"'

            if status == "SUCCESS":
                latency = f"{random.randint(20, 300)}ms"
                log_line += f' latency="{latency}"\n'
            else:
                err = random.choice(error_codes)
                log_line += f' error_code="{err}"\n'

            f.write(log_line)


if __name__ == "__main__":
    NUM_LINES = 10000  # Set this to 100,000 to test your script's performance!
    generate_apple_logs("apple_device_mgmt.log", NUM_LINES)
    print(f"Generated {NUM_LINES} log lines in apple_device_mgmt.log")
