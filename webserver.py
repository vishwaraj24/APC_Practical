
server_ip = ("192.168.1.10",)

allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips():
    ip = input("Enter new IP address to allow: ")
    allowed_ips.append(ip)
    print("IP added successfully!")

def display_config():
    print("\n----- Server Configuration -----")
    print("Server IP:", server_ip[0])
    print("Allowed IPs:", allowed_ips)

print("Current Configuration:")
display_config()

update_allowed_ips()

print("\nUpdated Configuration:")
display_config()