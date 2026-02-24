# A Cybersecurity Beginner Project: 
# 1. Define Rules 
# 2. Simulate Traffic 
# 3. Evaluate + Act
# 4. Evaluate Results
# 5. Please update as you go
# 6. Have Fun as you View this as a learning experience and not a test.

import random

print("Welcome to the Cybersecurity Beginner Project!")

import random

def generate_random_ip():
    """Generate a random IP address."""
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    """Check if the IP address matches any firewall rule and return the action."""
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"  # Default action if no rule matches

def main():
    # Define the firewall rules (key: IP address, value: action)
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

      # Simulate network traffic
    for _ in range(12):
     ip_address = generate_random_ip()
     action = check_firewall_rules(ip_address, firewall_rules)
     random_number = random.randint(0, 9999)
     print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()