import os
import sys
from PIL import Image
import concurrent

#Tuple of format types to check if file img format. Also.endswith works with tuple.
sup_img_type = (".jpg", ".png")

#Function to go through a directory, change format, size, and rotation of image.
def correct_images(directory, img_format, size, rotation):
    # directory = os.path.dirname(__file__)
    print(directory)
    if os.path.exists(directory):
        for input_file in os.listdir(directory):
            if input_file.endswith(sup_img_type):
                print(input_file)
                f, e = os.path.splitext(input_file)
                output_file = f + "_flipped_resized" + img_format
                try:
                    with Image.open(input_file) as im:
                        print("Correcting: " + input_file + " | Renaming to: " + output_file)
                        im.rotate(rotation).resize(size).save(output_file)
                except OSError as e:
                    print("Error Correcting: " + input_file)
                    print(e)
            else:
                continue
    else:
        print("Not a valid Path: {}".format(directory))

# Ask for inputs in case someone hasn't used the file before.
if __name__ == "__main__":
    correct_images(
        directory = os.getcwd(),
        img_format = input("What is the specified format: "),
        size = tuple(map(int,input("What is the size for the images: ").split(','))),
        rotation = int(input("Specify the rotation of the images: "))
    )