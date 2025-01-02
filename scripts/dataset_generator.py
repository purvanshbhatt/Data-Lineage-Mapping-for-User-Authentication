import random
import datetime
import hashlib

# Configuration for dataset generation
num_records = 10000  # Adjust the number of records as needed
start_time = datetime.datetime(2024, 11, 20, 10, 0, 0)
time_interval = datetime.timedelta(minutes=1)
resources = ['/login', '/dashboard', '/profile', '/settings', '/logout']
statuses = ['success', 'failed']

def generate_ip():
    """Generate a random IP address."""
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_username(index):
    """Generate a username."""
    #return f"user{index}"
    return hashlib.md5(str(index).encode()).hexdigest()[:8]

# Generate dataset
dataset = []
used_ips = set()  # Ensure unique IPs
current_time = start_time

for i in range(1, num_records + 1):
    # Ensure unique IPs
    while True:
        ip_address = generate_ip()
        if ip_address not in used_ips:
            used_ips.add(ip_address)
            break

    username = generate_username(i % 100 + 1)  # Rotate among 50 users
    status = random.choice(statuses)
    resource = random.choice(resources)
    
    # Create a record
    record = f"{current_time},{ip_address},{username},{status},{resource}"
    dataset.append(record)
    
    # Increment timestamp
    current_time += time_interval

# Save to a file
output_file = "datasets/web_server_logs.csv"
with open(output_file, "w") as f:
    f.write("timestamp,ip_address,username,status,resource_accessed\n")  # Header
    f.write("\n".join(dataset))

print(f"Dataset with {num_records} records saved to {output_file}")
