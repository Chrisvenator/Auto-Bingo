import os
import sys
import random
from PIL import Image, ImageDraw

# Get the input directory from the command line arguments
if len(sys.argv) < 3:
    print("Please provide the input directory and output name as command line arguments.")
    sys.exit(1)

input_dir = sys.argv[1]
output_name = sys.argv[2]

# Get a list of files in the input directory
files = os.listdir(input_dir)

# Shuffle the files list for different order
random.shuffle(files)

# Calculate the dimensions for the grid and spacing
grid_size = (6, 6)
spacing = 50
image_size = (250, 250)
extension_percentage = 0.05
border_thickness = 10

# Randomly select 25 images (if available) for the first collage
selected_files = random.sample(files, min(grid_size[0] * grid_size[1], len(files)))

# Calculate the extended image size
extended_image_size = (
    int(image_size[0] * (1 + extension_percentage)),
    int(image_size[1] * (1 + extension_percentage))
)

# Calculate the size of the final collage image
collage_width = grid_size[0] * extended_image_size[0] + (grid_size[0] - 1) * spacing
collage_height = grid_size[1] * extended_image_size[1] + (grid_size[1] - 1) * spacing
collage_size = (collage_width, collage_height)

# Create a new blank image for the first collage
collage1 = Image.new("RGBA", collage_size, (0, 0, 0, 0))

# Open the background image
background_path = "background.png"
background = Image.open(background_path).resize(collage_size)

# Make the background image 20% transparent
background = background.convert("RGBA")
background_with_transparency = Image.new("RGBA", background.size)
for x in range(background.width):
    for y in range(background.height):
        r, g, b, a = background.getpixel((x, y))
        background_with_transparency.putpixel((x, y), (r, g, b, int(a * 0.5)))

# Paste the background with transparency onto the first collage
collage1.paste(background_with_transparency, (0, 0))

# Iterate over the selected files and paste them onto the first collage
for i, file in enumerate(selected_files):
    # Calculate the position to paste the current image
    x = (i % grid_size[0]) * (extended_image_size[0] + spacing)
    y = (i // grid_size[0]) * (extended_image_size[1] + spacing)
    position = (x, y)

    # Open the image file
    image_path = os.path.join(input_dir, file)
    image = Image.open(image_path)

    # Calculate the extended background size
    extended_background_size = (
        int(extended_image_size[0] + 2 * (extension_percentage * image_size[0])),
        int(extended_image_size[1] + 2 * (extension_percentage * image_size[1]))
    )

    # Create a new image with extended background
    extended_image = Image.new("RGBA", extended_background_size, (0, 0, 0, 0))

    # Calculate the position to paste the image on the extended background
    image_position = (
        int(extension_percentage * image_size[0]) + 3,
        int(extension_percentage * image_size[1])
    )

    # Paste the image onto the extended background
    extended_image.paste(image, image_position)

    # Resize the extended image to the desired size
    resized_image = extended_image.resize(extended_image_size)

    # Create a new image with rounded rectangle border
    border_image = Image.new("RGBA", extended_image_size, (0, 0, 0, 0))
    border_draw = ImageDraw.Draw(border_image)
    border_radius = 20
    border_draw.rounded_rectangle(
        [(0, 0), (extended_image_size[0] - 1, extended_image_size[1] - 1)],
        border_radius,
        fill=None,  # Set fill to None for transparent fill
        outline=(255, 165, 0, 255),  # Set alpha to 255 (fully opaque)
        width=border_thickness  # Set the border thickness
    )

    # Composite the border image onto the first collage
    collage1.alpha_composite(border_image, position)

    # Create a new image with orange background and 20% transparency
    orange_background = Image.new("RGBA", extended_image_size, (255, 165, 0, int(0.2 * 255)))

    # Composite the resized image onto the orange background
    orange_background.paste(resized_image, (0, 0), resized_image)

    # Composite the image with orange background onto the first collage
    collage1.alpha_composite(orange_background, position)

# Save the first collage image
output_dir = "./out"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
collage1.save("out/" + output_name + "_1.png")

print("First collage created and saved as " + output_name + "_1.png.")

# Randomly select 25 images (if available) for the second collage
#selected_files = random.sample(files, min(25, len(files)))
random.shuffle(selected_files)

# Create a new blank image for the second collage
collage2 = Image.new("RGBA", collage_size, (0, 0, 0, 0))

# Paste the background with transparency onto the second collage
collage2.paste(background_with_transparency, (0, 0))

# Iterate over the selected files and paste them onto the second collage
for i, file in enumerate(selected_files):
    # Calculate the position to paste the current image
    x = (i % grid_size[0]) * (extended_image_size[0] + spacing)
    y = (i // grid_size[0]) * (extended_image_size[1] + spacing)
    position = (x, y)

    # Open the image file
    image_path = os.path.join(input_dir, file)
    image = Image.open(image_path)

    # Calculate the extended background size
    extended_background_size = (
        int(extended_image_size[0] + 2 * (extension_percentage * image_size[0])),
        int(extended_image_size[1] + 2 * (extension_percentage * image_size[1]))
    )

    # Create a new image with extended background
    extended_image = Image.new("RGBA", extended_background_size, (0, 0, 0, 0))

    # Calculate the position to paste the image on the extended background
    image_position = (
        int(extension_percentage * image_size[0]) + 3,
        int(extension_percentage * image_size[1])
    )

    # Paste the image onto the extended background
    extended_image.paste(image, image_position)

    # Resize the extended image to the desired size
    resized_image = extended_image.resize(extended_image_size)

    # Create a new image with rounded rectangle border
    border_image = Image.new("RGBA", extended_image_size, (0, 0, 0, 0))
    border_draw = ImageDraw.Draw(border_image)
    border_radius = 20
    border_draw.rounded_rectangle(
        [(0, 0), (extended_image_size[0] - 1, extended_image_size[1] - 1)],
        border_radius,
        fill=None,  # Set fill to None for transparent fill
        outline=(255, 165, 0, 255),  # Set alpha to 255 (fully opaque)
        width=border_thickness  # Set the border thickness
    )

    # Composite the border image onto the second collage
    collage2.alpha_composite(border_image, position)

    # Create a new image with orange background and 20% transparency
    orange_background = Image.new("RGBA", extended_image_size, (255, 165, 0, int(0.2 * 255)))

    # Composite the resized image onto the orange background
    orange_background.paste(resized_image, (0, 0), resized_image)

    # Composite the image with orange background onto the second collage
    collage2.alpha_composite(orange_background, position)

# Save the second collage image
collage2.save("out/" + output_name + "_2.png")

print("Second collage created and saved as " + output_name + "_2.png.")
