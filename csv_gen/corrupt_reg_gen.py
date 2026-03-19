import csv
import random


def generate_apple_telemetry(filename, n_rows=1000):
    regions = ["us-east-1", "us-west-2", "eu-central-1", "ap-northeast-1"]
    # We'll create 10 specific clusters to see if your logic groups them correctly
    cluster_ids = [f"cluster-{i:03d}" for i in range(1, 11)]

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["vm_id", "cluster_id", "region",
                        "cpu_usage", "monthly_cost"])

        for i in range(n_rows):
            vm_id = f"vm-{i:06d}"
            c_id = random.choice(cluster_ids)
            reg = random.choice(regions)

            # Simulate data corruption (5% chance of NULL or empty)
            corruption_roll = random.random()
            if corruption_roll < 0.03:
                cpu = "NULL"
            elif corruption_roll < 0.05:
                cpu = ""
            else:
                # Simulate "Underutilized" clusters (low CPU) vs "Busy" clusters
                # Cluster-001 and Cluster-002 will be our "candidates" (mostly low CPU)
                if c_id in ["cluster-001", "cluster-002"]:
                    cpu = round(random.uniform(1.0, 9.5), 2)
                else:
                    cpu = round(random.uniform(5.0, 85.0), 2)

            cost = round(random.uniform(50.0, 500.0), 2)

            writer.writerow([vm_id, c_id, reg, cpu, cost])

    print(f"✅ Generated {filename} with {n_rows} rows.")


# Generate a test file with 10,000 rows
generate_apple_telemetry("telemetry.csv", n_rows=10000)
