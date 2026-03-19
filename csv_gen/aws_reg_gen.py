import csv
import random


def generate_sample_data(filename="cloud_inventory.csv", num_rows=1000):
    regions = ["us-east-1", "us-west-2", "eu-central-1", "ap-northeast-1"]
    statuses = ["running", "stopped", "terminated", "pending"]

    headers = ["vm_id", "region", "status", "uptime_days", "monthly_cost"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for i in range(1, num_rows + 1):
            writer.writerow({
                "vm_id": f"i-{random.getrandbits(32):x}",  # Mimics AWS hex IDs
                "region": random.choice(regions),
                "status": random.choice(statuses),
                "uptime_days": random.randint(0, 365),
                "monthly_cost": round(random.uniform(10.0, 500.0), 2)
            })

    print(f"✅ Success: {filename} created with {num_rows} rows.")


# Run this once to create your file
generate_sample_data(num_rows=1000)
