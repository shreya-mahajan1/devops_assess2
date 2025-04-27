import os
import datetime

current_directory = os.getcwd()

current_time = datetime.datetime.now()

print(f"Current Directory: {current_directory}")
print(f"Current Timestamp: {current_time}")
print("Hello from Jenkins!")
