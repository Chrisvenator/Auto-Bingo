import subprocess
import os
import sys
import shutil

if len(sys.argv) < 2:
    print("Please provide the input directory and output name as command line arguments.")
    sys.exit(1)

input_dir = sys.argv[1]

# Specify the directories to compare
directory1 = input_dir
directory2 = "./" + input_dir + "-processed"

if not os.path.exists(directory2):
    os.makedirs(directory2)

# Get the list of filenames in each directory
files1 = set(os.listdir(directory1))
files2 = set(os.listdir(directory2))


files1 = set([os.path.splitext(file)[0] for file in files1])
files2 = set([os.path.splitext(file)[0] for file in files2])


# Check if all the filenames are the same
if files1 != files2 or not os.path.exists(directory2) or not os.path.isdir(directory2): 
    print("Processing images for " + directory1)
    shutil.rmtree(directory2)
    subprocess.call(["python", "preprocess_images.py", directory1])
    print("Processed images for " + directory1)