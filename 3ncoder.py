# This is a program that converts converts a user input in different Encoding schemes:
import base64
import urllib2
import time
from urllib import quote
time.sleep(3)
print "Welcome! Encode your input and rot in hell !\n\n "
time.sleep(2)
Input=raw_input("Enter your payload, Master !!\n\n")
print "\n\nProcessing.......Sit Back & Relax !!"
time.sleep(2)
Base64=base64.b64encode(Input)
URLencode=urllib2.quote(Input)
HTML=quote(Input)
print "The HTML encoded value is as below: \n", HTML
print "The Base64 encoded value is as below: \n", Base64
print "The URLencoded value is as below: \n", URLencode
print "\nJob Done !! "
