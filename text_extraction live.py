from PIL import Image 
import cv2
from pytesseract import pytesseract 
import time 

def text_finder():

    print("starting text extraction")
    # Defining paths to tesseract.exe 
    # and the image we would be using 
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    cap = cv2.VideoCapture(0)

    time.sleep(3)
    ret, frame = cap.read()
    if ret != True:
        raise ValueError("Can't read frame")

    cv2.imshow("img1", frame)



    
    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = pytesseract.image_to_string(frame)

    print(text)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()



text_finder()
