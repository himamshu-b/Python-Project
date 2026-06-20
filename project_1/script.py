# This is to generate random logs in python
import random
import datetime
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = [
    "User logged in successfully.",
    "Database connection timeout.",
    "Failed to load configuration profile.",
    "API request processed in 45ms.",
    "Memory usage exceeded threshold limit.",
    "File asset uploaded cleanly."
]
print("Generating logs.txt file...")
with open("logs.txt", "w") as file:
    # Loop to generate 100 random lines of logs
    for i in range(100):
        timestamp = datetime.datetime.now() - datetime.timedelta(minutes=i)
        level = random.choice(log_levels)
        msg = random.choice(messages)
        
        # Format the line exactly like a real enterprise system server log
        log_line = f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {level}: {msg}\n"
        file.write(log_line)

print("Done! Open 'logs.txt' to see your new dataset.")