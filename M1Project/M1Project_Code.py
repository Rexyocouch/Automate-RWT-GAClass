import os
import sys

from PIL import Image
from concurrent import futures

#Tuple of format types to check if file img format. Note: .endswith works with tuple.
sup_img_type = (".jpg", ".png")

#Text being added to filename.
file_add_info = "_flipped_resized"

#Function to go through a directory, change format, size, and rotation of image.
def correct_images(directory, img_format, size, rotation):
    print(directory)
    executor = futures.ThreadPoolExecutor()
    if os.path.exists(directory):
        for input_file in os.listdir(directory):
            if input_file.endswith(sup_img_type):
                print(input_file)
                f, e = os.path.splitext(input_file)
                output_file = f + file_add_info + img_format
                try:
                    with Image.open(input_file) as im:
                        print("Correcting: " + input_file + " | Renaming to: " + output_file)
                        executor.submit(im.rotate(rotation).resize(size).save(output_file))
                except OSError as e:
                    print("Error Correcting: " + input_file)
                    print(e)
            else:
                continue
    else:
        print("Not a valid Path: {}".format(directory))
    print("Waiting for all workers to finish.")
    executor.shutdown()

# Ask for inputs to make it a bit easier on the user.
if __name__ == "__main__":
    correct_images(
        #Script execution location is being used as the directory.
        directory = os.getcwd(),
        img_format = input("What is the specified format? Ex:.jpg: "),
        size = tuple(map(int,input("What is the size for the images? Ex:1920,1080: ").split(','))),
        rotation = int(input("Specify the rotation of the images? Ex:90: "))
    )
