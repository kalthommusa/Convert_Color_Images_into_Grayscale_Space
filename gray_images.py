# Import the necessary packages
import cv2
import glob
import argparse
import os


# Creat a parser
parser = argparse.ArgumentParser(description="Convert multiple images into grayscale")
# Optional arguments 
parser.add_argument("-i", "--input", help="path to the input images folder")
parser.add_argument("-o", "--output", help="path to the output images folder")

args = parser.parse_args()

# Path to the input folder
path = args.input+"*.*"

# Path to the output folder
outpath = args.output

# Check if the given directory exists
if os.path.isdir(outpath) != True:
	print("This folder {} does not exist, please provide an existing folder.".format(outpath))


# Initialize a counter for images 
img_num = 1

# Using glob module with for loop to fetch each image from the input folder
for file in glob.glob(path):
	try:
		# Read(load) each image
		read_img = cv2.imread(file)
		# Convert each image into grayscale
		gray_img = cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)
		# Write(save) each of the converted images in the given output path folder
		cv2.imwrite(outpath+"gray_image"+str(img_num)+".jpeg", gray_img)
	except:
		print ("{} is not converted".format(file))
