import csv
import hashlib

def generate_password_hash(password):
    """Generates a password hash using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_user_data(input_file, output_file):
    """Generates user data from web server logs."""
    users = {}
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['username']
            if username not in users:
                users[username] = {'password_hash': generate_password_hash(username), 'last_login': ''}

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['username', 'password_hash', 'last_login']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for username, data in users.items():
            last_login = '2024-11-20 00:00:00'  # Default last login
            writer.writerow({'username': username, 'password_hash': data['password_hash'], 'last_login': last_login})

if __name__ == "__main__":
    input_file = "datasets/web_server_logs.csv"
    output_file = "datasets/user_data.csv"
    generate_user_data(input_file, output_file)
