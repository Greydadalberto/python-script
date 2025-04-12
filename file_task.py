import os
import requests
from datetime import datetime

# 1. Create custom directory
first_name = "Derrick"
last_name = "Darku"
directory_name = f"{first_name}_{last_name}"

if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directory '{directory_name}' created.")
else:
    print(f"Directory '{directory_name}' already exists.")

# 2. Download the file
file_url = "https://github.com/Greydadalberto/python-script"  # Replace with actual URL
response = requests.get(file_url)

if response.status_code == 200:
    file_path = os.path.join(directory_name, f"{first_name}_{last_name}.txt")
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"File downloaded and saved as {file_path}")
else:
    print("Failed to download the file.")

# 3. Modify file content
user_input = input("Describe what you have learned so far in a sentence:\n")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_content = f"{user_input}\n\nLast updated: {timestamp}"

with open(file_path, "w") as file:
    file.write(new_content)
print("File content updated.")

# 4. Verify content
with open(file_path, "r") as file:
    print("\nFinal File Content:\n" + "-"*25)
    print(file.read())

