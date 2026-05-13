from datetime import datetime
import random
import os

messages = [
    "Improved project notes",
    "Updated learning logs",
    "Refined documentation",
    "Added new progress entry",
    "Worked on automation",
    "Updated development journal",
    "Improved workflow setup",
    "Added coding insights",
]

folders = [
    "logs",
    "notes",
    "journal",
]

# Create folders if missing
for folder in folders:
    os.makedirs(folder, exist_ok=True)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

filename = random.choice(folders) + "/activity.md"

entry = f"""
## {now}

{random.choice(messages)}

---
"""

with open(filename, "a", encoding="utf-8") as f:
    f.write(entry)

print(f"Updated {filename}")