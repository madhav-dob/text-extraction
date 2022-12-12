from PIL import Image 
import cv2
from pytesseract import pytesseract 
import time 

def text_finder():

    print("starting text extraction")
    # Defining paths to tesseract.exe 
    # and the image we would be using 
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # provide the image path below
    image_path = r"C:\Users\surbhi\Desktop\1.jpg"
    my_image = Image.open(image_path)
    # Opening the image & storing it in an image object 

    # Providing the tesseract executable 
    # location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract 
    
    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = pytesseract.image_to_string(my_image)
    #text = "here i am"
    # Displaying the extracted text 
    print(text[:-1])
    return text


text_finder()