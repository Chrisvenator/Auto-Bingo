import os
import sys
from PIL import Image

# Create the output directory if it doesn't exist
# Get the input directory from the command line arguments
if len(sys.argv) < 2:
    print("Please provide the input directory as a command line argument.")
    sys.exit(1)

input_dir = sys.argv[1]

output_dir = "./" + input_dir + "-processed"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    



# Get a list of files in the input directory
files = os.listdir(input_dir)

for file in files:
    # Check if the file is an image (assumes all files in the directory are images)
    if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Open the image file
        image_path = os.path.join(input_dir, file)
        image = Image.open(image_path)

        # Resize the image to 250x250 pixels
        resized_image = image.resize((250, 250))

        # Generate the output file path
        output_file = os.path.join(output_dir, os.path.splitext(file)[0] + ".png")

        # Save the resized image as PNG
        resized_image.save(output_file, "PNG")

        #print(f"Processed {file} and saved as {output_file}")
