import subprocess
import os
import random


subprocess.call(["python", "check_for_changes.py", "city"])
subprocess.call(["python", "check_for_changes.py", "countryside"])

print("Auto-Bingo creation:")

# Call the script with the input_dir as a command-line argument
subprocess.call(["python", "create_grid.py", os.path.join("countryside-processed"), "countryside-" + str(random.randint(100000, 1000000))])
subprocess.call(["python", "create_grid.py", os.path.join("city-processed"), "city-" + str(random.randint(100000, 1000000))])

print("Auto-Bingo creation complete")