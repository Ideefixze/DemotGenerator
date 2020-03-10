'''
# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://maps.googleapis.com/maps/api/geocode/json"
  
# location given here 
location = "dobrzechow 201"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'key':'AIzaSyA1NY_HT5adb0oD-pZT79AlddsO1KaAlAI','address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 
#print(r.json())
  
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
latitude = data['results'][0]['geometry']['location']['lat'] 
longitude = data['results'][0]['geometry']['location']['lng'] 
formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address)) 

'''
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = 'D:\\pyquests\\src\\image4.jpg'

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description + " " + str(label.topicality))

