import time
import random
import os

# The file where logs will be stored
LOG_FILE = "server_logs.txt"

# Typical cloud event types
events = [
    "INFO: User 'admin' logged in from 192.168.1.1",
    "INFO: Database backup completed successfully.",
    "WARNING: Failed login attempt from IP 45.33.22.11",
    "INFO: New container 'web-srv-01' started.",
    "CRITICAL: Unauthorized access attempt on /etc/passwd",
    "WARNING: High CPU usage detected on 'db-master'",
    "CRITICAL: SQL Injection pattern detected in query string"
]

print("--- Mock Cloud Server Started ---")
print(f"Writing logs to {LOG_FILE}... (Press Ctrl+C to stop)")

# Ensure the file is fresh
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

while True:
    with open(LOG_FILE, "a") as f:
        event = random.choice(events)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {event}\n"
        
        f.write(log_entry)
        print(f"LOGGED: {log_entry.strip()}")
    
    # Generate a new log every 2 seconds
    time.sleep(2)


if _name_ == "_main_":
    # Render automatically sets a PORT
    port = int(os.environ.get("PORT", 10000))
    # '0.0.0.0' is required for Render to detect the app
    # Agar aap Flask use kar rahi hain:
    app.run(host='0.0.0.0', port=port)
    # Agar simple script hai toh:
    # print(f"Login service started on port {port}")
