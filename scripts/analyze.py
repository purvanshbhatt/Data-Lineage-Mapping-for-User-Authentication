import pandas as pd
import re
import os

# 1. Load the data
data_dir = os.path.join(os.path.dirname(__file__), 'datasets')
web_data = pd.read_csv(os.path.join(data_dir, 'web_server_logs.csv'))
user_data = pd.read_csv(os.path.join(data_dir, 'user_data.csv'))

# 2. Login success/failure analysis
total_logins = len(web_data)
successful_logins = len(web_data[web_data['status'] == 'success'])
success_rate = (successful_logins / total_logins) * 100
print(f"Success rate: {success_rate:.2f}%")

failed_logins = web_data[web_data['status'] == 'failed']
failed_attmpts_per_user = failed_logins.groupby('username')['status'].count()

users_with_multiple_fails = failed_attmpts_per_user[failed_attmpts_per_user > 2]
print("\nUsers with multiple failed login attempts:")
print(users_with_multiple_fails)

# 3. User activity analysis
successful_logins = web_data[web_data['status'] == 'success']
resource_access_count = successful_logins.groupby('resource_accessed').size()
print("\nResource access counts:")
print(resource_access_count)

# 4. Time series analysis
web_data['timestamp'] = pd.to_datetime(web_data['timestamp'])
login_attempt_hourly = web_data.groupby(pd.Grouper(key='timestamp', freq='H')).size()
print("\nLogin attempts per hour:")
print(login_attempt_hourly)

# 5. Correlation with 'last_login' 
merged_data = pd.merge(user_data, web_data, on='username')
print("\nMerged Data (web data and user credentials):")
print(merged_data.head())

# 6.  SQL Injection Analysis
sql_injection_pattern = re.compile(r"['\"\-;]|-\;|\*/|/\*")
suspecious_request = web_data[web_data['resource_accessed'].str.contains(sql_injection_pattern, na=False)]

if not suspecious_request.empty:
    print("\nPotential SQL Injection Attacks detected:")
    print(suspecious_request)
else:
    print("\nNo potential SQL Injection Attacks detected.")

# 7. Brute force attack analysis
failed_logins = web_data[web_data['status'] == 'failed']
failed_attempts_per_ip_hour = failed_logins.groupby(['ip_address', pd.Grouper(key='timestamp', freq='H')]).size()

suspicious_ips = failed_attempts_per_ip_hour[failed_attempts_per_ip_hour > 10]

print("\nPotential brute-force attacks:")
print(suspicious_ips)

# 8. Cross-site scripting (XSS) attack analysis
xss_pattern = re.compile(r"<script>|alert\(|</script>")
suspecious_request = web_data[web_data['resource_accessed'].str.contains(xss_pattern, na=False)]

if not suspecious_request.empty:
    print("\nPotential XSS Attacks detected:")
    print(suspecious_request)



