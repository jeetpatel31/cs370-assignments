from PIL import Image
import numpy as np
import random
import os

# Define the directory with the images and where to save them
input_dir = "detected_objects"
output_dir_deconstructed = "deconstructed"
output_dir_reconstructed = "reconstructed_with_gaps"

# Create output directories if they do not exist
os.makedirs(output_dir_deconstructed, exist_ok=True)
os.makedirs(output_dir_reconstructed, exist_ok=True)

# Function to deconstruct and reconstruct an image
def process_image(image_path, output_name):
    image = Image.open(image_path)
    
    # Calculate the size of each box
    width, height = image.size
    box_width = width // 3
    box_height = height // 3
    
    # Split the image into 9 boxes and track their positions
    boxes = [(image.crop((j * box_width, i * box_height, (j + 1) * box_width, (i + 1) * box_height)))
             for i in range(3) for j in range(3)]
    
    # Shuffle the boxes
    shuffled_boxes = random.sample(boxes, len(boxes))
    
    # Deconstruct the image
    deconstructed_image = Image.new('RGB', (width, height))
    for i, box in enumerate(shuffled_boxes):
        x = (i % 3) * box_width
        y = (i // 3) * box_height
        deconstructed_image.paste(box, (x, y))
    
    # Save the deconstructed image
    deconstructed_image.save(os.path.join(output_dir_deconstructed, output_name + "_deconstructed.png"))
    
    # Reconstruct the image with gaps
    gap = 10
    new_width = width + gap * 2
    new_height = height + gap * 2
    reconstructed_image = Image.new('RGB', (new_width, new_height), "white")
    
    # Place the boxes back in their original order with gaps
    for i, box in enumerate(boxes):
        x = (i % 3) * (box_width + gap)
        y = (i // 3) * (box_height + gap)
        reconstructed_image.paste(box, (x, y))
    
    # Save the reconstructed image with gaps
    reconstructed_image.save(os.path.join(output_dir_reconstructed, output_name + "_reconstructed.png"))

# Process each image in the directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        file_path = os.path.join(input_dir, filename)
        output_name, _ = os.path.splitext(filename)
        process_image(file_path, output_name)
