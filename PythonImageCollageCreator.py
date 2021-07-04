# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO CREATE THE COLLAGE OF USER SELECTED IMAGES USING THE PIL AND numpy LIBRARIES

# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.
# The Image module provides a class with the same name which is used to represent a PIL image. The module also
# provides a number of factory functions, including functions to load images from files, and to create new images.
# Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object,
# and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

# Importing necessary packages
import numpy as np
from PIL import Image

# Defining create_collage() function with to create the collage images_list and collage_name as arguments
def create_collage(images_list, collage_name):
    # Displaying the list of user entered images with path
    print("\nLIST OF IMAGES ENTERED BY THE USER : ")
    for image in images_list:
        print(image)
    # Creating an empty list called image_array_list
    image_array_list = []
    # Looping through each image item in the list
    for image in images_list:
        # Opening the image using the open() method of Image Class which takes ImagePathName as argument
        image_obj = Image.open(image)
        # Creating the array of the Image Object using the array() of numpy module by passing image_obj
        image_array = np.array(image_obj)
        # Adding the Image Array to the created list called image_list
        image_array_list.append(image_array)
    # Arranging arrays of images in sequence vertically (row-wise)
    image_stack = np.row_stack(image_array_list)
    # Creating the image_stack array using the fromarray() method of Image Library
    image_collage = Image.fromarray(image_stack)
    # Saving the resulting collage image using the save() which takes the collage_name as argument
    image_collage.save(collage_name)
    # Opening the image using the open() method of Image Class which takes ImagePathName as argument
    collage_image_obj = Image.open(collage_name)
    # Displaying the COLLAGE IMAGE
    collage_image_obj.show()
    print("\nCOLLAGE CREATED AND SAVED SUCCESSFULLY")

# Driver Code
if __name__ == '__main__':
    # Creating an empty list called input_list
    input_list = []
    # Prompting the user to enter the image name with path
    print("IMAGE NAME WITH PATH IN NEW LINES : ")
    while True:
        input_image_path = input()
        if input_image_path == "done":
            break
        # Adding the input to the list input_list
        input_list.append(input_image_path)
    # Prompting the user to enter the collage image name with path
    collage_image_name = input("\nCOLLAGE IMAGE NAME WITH PATH : ")
    # Calling the create_collage() with the list of images and collage_name as the arguments
    create_collage(input_list, collage_image_name)