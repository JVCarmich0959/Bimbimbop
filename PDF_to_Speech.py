# This script will read a PDF file and convert it to an audio file using pyttsx3
# You can use this script to convert any PDF file to an audio file for your personal 
# use or for your students who are visually impaired or have learning disabilities.

# This script is based on the following tutorial:
# https://www.youtube.com/watch?v=Z2X4Xv5ZGKU:



# import the required libraries
import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('Natural_Language_Processing_in_Action_S_v7.pdf', 'rb')) # open the PDF file
speaker = pyttsx3.init() # initialize the pyttsx3 engine

# Concatenate the text from all pages
all_text = ""
for page_num in range(len(pdfreader.pages)):
    all_text += pdfreader.pages[page_num].extract_text()

speaker.say(all_text) # say the concatenated text
speaker.runAndWait() # wait for the pyttsx3 engine to finish speaking the text

speaker.stop() # stop the pyttsx3 engine

