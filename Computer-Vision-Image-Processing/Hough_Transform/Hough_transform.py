"""
CS136 Term Project - Hough Transform: Edges and Lines
-----------------------------------------------------

This program applies Hough Line Transform to all 4 project images.

It saves only 2 output images for each input image:

1. image_hough_edges.jpg
   - The Canny edge image used as input for Hough Transform.

2. image_hough_lines.jpg
   - The original image with detected Hough lines drawn in green.

Important:
The DW image is a geology image with many natural rock textures.
If Hough settings are too loose, it detects too many lines.
If Hough settings are too strict, it detects almost no lines.

For DW.jpg, this version uses balanced parameters:
- higher Canny thresholds to reduce weak texture edges
- moderate Hough threshold
- longer minimum line length
- small maximum line gap

Required folder structure:

CS136_Term_Project/
│
├── Input_Images/
│   ├── coastline.jpg
│   ├── tahoe.jpg
│   ├── DW.jpg
│   └── marine_brood.jpg
│
└── Hough_Transform/
    ├── Hough_transform.py
    └── Hough_Images/

How to run from terminal:

python3 Hough_Transform/Hough_transform.py

or:

python Hough_Transform/Hough_transform.py
"""

import cv2
import numpy as np
from pathlib import Path


# --------------------------------------------------
# Folder paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_DIR = BASE_DIR / "input_images"
OUTPUT_DIR = BASE_DIR / "Hough_Transform" / "Hough_Images"

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
# Per-image parameters
# --------------------------------------------------
# Each image has different texture levels, so using the same Hough
# parameters for every image does not always give the best result.
#
# Parameters:
# canny_low, canny_high:
#   Thresholds for the Canny edge detector.
#
# hough_threshold:
#   Minimum number of votes needed to accept a line.
#
# min_line_length:
#   Minimum length of detected line segments.
#
# max_line_gap:
#   Maximum gap between line segments that can still be connected.
#
# line_thickness:
#   Thickness of green lines drawn on the output image.

params = {
    "coastline.jpg": {
        "canny_low": 50,
        "canny_high": 150,
        "hough_threshold": 80,
        "min_line_length": 80,
        "max_line_gap": 10,
        "line_thickness": 2
    },

    "tahoe.jpg": {
        "canny_low": 80,
        "canny_high": 180,
        "hough_threshold": 100,
        "min_line_length": 120,
        "max_line_gap": 8,
        "line_thickness": 2
    },

    # Balanced DW settings:
    # These values reduce clutter but still allow visible detected lines.
    "DW.jpg": {
        "canny_low": 100,
        "canny_high": 220,
        "hough_threshold": 115,
        "min_line_length": 130,
        "max_line_gap": 8,
        "line_thickness": 2
    },

    "marine_brood.jpg": {
        "canny_low": 50,
        "canny_high": 150,
        "hough_threshold": 80,
        "min_line_length": 80,
        "max_line_gap": 10,
        "line_thickness": 2
    }
}


# --------------------------------------------------
# Apply Hough Line Transform
# --------------------------------------------------

for image_name in image_files:
    image_path = INPUT_DIR / image_name

    # Read image
    image = cv2.imread(str(image_path))

    if image is None:
        print(f"Error: Could not read {image_path}")
        print("Check that the image exists and the file name is correct.")
        continue

    # Copy image for drawing detected lines
    line_output = image.copy()

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smooth image before edge detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Get image-specific parameters
    p = params[image_name]

    # Canny edge detection
    edges = cv2.Canny(
        blurred_image,
        p["canny_low"],
        p["canny_high"]
    )

    # Probabilistic Hough Line Transform
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=p["hough_threshold"],
        minLineLength=p["min_line_length"],
        maxLineGap=p["max_line_gap"]
    )

    line_count = 0

    # Draw detected lines in green
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(
                line_output,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                p["line_thickness"]
            )
            line_count += 1

    # Save only edge and line outputs
    stem = image_path.stem

    edge_output_path = OUTPUT_DIR / f"{stem}_hough_edges.jpg"
    line_output_path = OUTPUT_DIR / f"{stem}_hough_lines.jpg"

    cv2.imwrite(str(edge_output_path), edges)
    cv2.imwrite(str(line_output_path), line_output)

    print(f"Processed: {image_name}")
    print(f"  Canny thresholds: {p['canny_low']}, {p['canny_high']}")
    print(f"  Hough threshold: {p['hough_threshold']}")
    print(f"  Min line length: {p['min_line_length']}")
    print(f"  Max line gap: {p['max_line_gap']}")
    print(f"  Lines detected: {line_count}")
    print(f"  Saved edge image: {edge_output_path}")
    print(f"  Saved line image: {line_output_path}")
    print()


print("Hough Line Transform completed for all images.")
