import sys
import os
import cv2 as cv

from Chroma3 import Image
import matplotlib.pyplot as plt
import numpy as np

def process_image(input_path, output_folder):
    img = Image(cv.imread(input_path))

    plt.subplot(2, 2, (1, 2))
    plt.hist(img.h, density=True, bins=360)
    plt.title("Hue")
    plt.subplot(2, 2, 3)
    plt.hist(img.s, density=True, bins=50)
    plt.title("Sat")
    plt.subplot(2, 2, 4)
    plt.hist(img.v, density=True, bins=50)
    plt.title("Val")

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    hist, xedges, yedges = np.histogram2d(img.h, img.s, bins=50)

    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0

    dx = dy = 0.25 * np.ones_like(zpos)
    dz = hist.ravel()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

    # Save the output image to the output folder
    output_path = os.path.join(output_folder, os.path.basename(input_path))
    plt.savefig(output_path)
    plt.close()

if len(sys.argv) > 2:
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        # Construct the full path to the input image
        input_path = os.path.join(input_folder, image_file)

        # Process each image and save the result to the output folder
        process_image(input_path, output_folder)
else:
    print("Please provide input and output folders as command-line arguments.")
