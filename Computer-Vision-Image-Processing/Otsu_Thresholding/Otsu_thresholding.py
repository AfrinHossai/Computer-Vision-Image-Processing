"""
CS136 Term Project - Otsu's Thresholding
----------------------------------------

This program applies Otsu's Thresholding to all 4 project images.

Otsu's Thresholding is an additional computer vision algorithm.
It automatically chooses the best threshold value to separate an image
into dark and bright regions.

Input folder:
Input_Images/

Output folder:
Otsu_Thresholding/Otsu_Thresholding_Images/

Required folder structure:

CS136_Term_Project/
│
├── Input_Images/
│   ├── coastline.jpg
│   ├── tahoe.jpg
│   ├── DW.jpg
│   └── marine_brood.jpg
│
└── Otsu_Thresholding/
    ├── Otsu_thresholding.py
    └── Otsu_Thresholding_Images/

How to run from terminal:

python3 Otsu_Thresholding/Otsu_thresholding.py

or:

python Otsu_Thresholding/Otsu_thresholding.py
"""

import cv2
from pathlib import Path


# --------------------------------------------------
# Set folder paths
# --------------------------------------------------

# Set project directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Folder containing original images
INPUT_DIR = BASE_DIR / "input_images"

# Folder where Otsu output images will be saved
OUTPUT_DIR = BASE_DIR / "Otsu_Thresholding" / "Otsu_Thresholding_Images"

# Create output folder if it does not already exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# Input image names
# --------------------------------------------------

image_files = [
    "coastline.JPG",
    "tahoe.JPG",
    "DW.jpg",
    "marine_brood.jpg"
]

# --------------------------------------------------
# Apply Otsu's Thresholding to each image
# --------------------------------------------------

for image_name in image_files:
    image_path = INPUT_DIR / image_name

    # Read original image
    image = cv2.imread(str(image_path))

    # Check if the image loaded correctly
    if image is None:
        print(f"Error: Could not read {image_path}")
        print("Check that the image exists and the file name is correct.")
        continue

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur before thresholding
    # This reduces small noise and helps Otsu's method perform better.
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Otsu's Thresholding
    # The threshold value is selected automatically by OpenCV.
    otsu_threshold_value, otsu_image = cv2.threshold(
        blurred_image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Create output file name
    output_name = image_path.stem + "_otsu.jpg"
    output_path = OUTPUT_DIR / output_name

    # Save thresholded image
    cv2.imwrite(str(output_path), otsu_image)

    print(f"Processed: {image_name}")
    print(f"  Otsu threshold value: {otsu_threshold_value}")
    print(f"  Saved Otsu image: {output_path}")
    print()


print("Otsu's Thresholding completed for all images.")
