"""
CS136 Term Project - Sobel Edge Detection
-----------------------------------------

This program applies Sobel edge detection to all 4 project images.

Input folder:
Input_Images/

Output folder:
Sobel_Edge_Detection/Sobel_Edge_Images/

Required folder structure:

CS136_Term_Project/
│
├── Input_Images/
│   ├── coastline.jpg
│   ├── tahoe.jpg
│   ├── DW.jpg
│   └── marine_brood.jpg
│
└── Sobel_Edge_Detection/
    ├── Sobel_edge_detection.py
    └── Sobel_Edge_Images/

How to run from terminal:

python Sobel_Edge_Detection/Sobel_edge_detection.py

If that does not work, use:

python3 Sobel_Edge_Detection/Sobel_edge_detection.py
"""

import cv2
import numpy as np
from pathlib import Path


# --------------------------------------------------
# Set folder paths
# --------------------------------------------------

# BASE_DIR means the main project folder: CS136_Term_Project
BASE_DIR = Path(__file__).resolve().parents[1]

# Folder containing original images
INPUT_DIR = BASE_DIR / "Input_Images"

# Folder where Sobel edge images will be saved
OUTPUT_DIR = BASE_DIR / "Sobel_Edge_Detection" / "Sobel_Edge_Images"

# Create output folder if it does not already exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# List of input images
# Make sure your image names match these names exactly
# --------------------------------------------------

image_files = [
    "coastline.jpg",
    "tahoe.jpg",
    "DW.jpg",
    "marine_brood.jpg"
]


# --------------------------------------------------
# Sobel parameters
# --------------------------------------------------

# Kernel size for Sobel operator.
# Common values are 3, 5, or 7.
# 3 is standard and preserves details well.
SOBEL_KERNEL_SIZE = 3


# --------------------------------------------------
# Apply Sobel edge detection to each image
# --------------------------------------------------

for image_name in image_files:
    image_path = INPUT_DIR / image_name

    # Read original image
    image = cv2.imread(str(image_path))

    # Check if image loaded correctly
    if image is None:
        print(f"Error: Could not read {image_path}")
        print("Check that the image exists and the file name is correct.")
        continue

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filter in x-direction
    sobel_x = cv2.Sobel(
        gray_image,
        cv2.CV_64F,
        1,
        0,
        ksize=SOBEL_KERNEL_SIZE
    )

    # Apply Sobel filter in y-direction
    sobel_y = cv2.Sobel(
        gray_image,
        cv2.CV_64F,
        0,
        1,
        ksize=SOBEL_KERNEL_SIZE
    )

    # Calculate gradient magnitude by combining x and y edges
    sobel_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    # Normalize result to range 0-255
    sobel_magnitude = cv2.normalize(
        sobel_magnitude,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    # Convert result to unsigned 8-bit image so it can be saved
    sobel_output = np.uint8(sobel_magnitude)

    # Create output file names
    output_name = image_path.stem + "_sobel.jpg"
    output_path = OUTPUT_DIR / output_name

    # Save final Sobel edge image
    cv2.imwrite(str(output_path), sobel_output)

    print(f"Saved Sobel edge image: {output_path}")


print("Sobel edge detection completed for all images.")
