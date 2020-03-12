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
import praw as p
import requests 
from tqdm import tqdm

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def Labeling():
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


def ZrobDemota():
    URL='http://www.demotmaker.com.pl/zaawansowane.php'
    PARAMS={'action':'lang=pl','obrazek':'2','tekst':'nowydemot','kolor1':'Biały',
    'kolor2':'Biały','rozmiar1':'36','rozmiar2':'16','opis':'test','plik':'','link':'https://i.redd.it/o5ni0epffwl41.jpg',
    'obrobka':'brak','obrot':'brak','kolorobr':'Czarne','rozmiarobr':'2','kolortla':'Czarne'}
    r = requests.post(url = URL, data=PARAMS, files = PARAMS)
    #print(r.request.body)
    #print(r.request.headers)
    #print(r.request.)
    #print(r.text)
    start = r.text.find("obrazki/")
    end = r.text.find("\"",start)
    print(start)
    print(end)

    url_part=r.text[start:end]

    img_response = requests.get("http://demotmaker.com.pl/"+url_part, stream=True)
    with open("D:\\pyquests\\src\\dls\\demot.jpg", "wb") as handle:
        for data in tqdm(img_response.iter_content()):
            handle.write(data)
    
def TEST():
    URL='http://ptsv2.com/t/Joseph/post'
    PARAMS={'aaa':'aaa'}
    r = requests.post(url = URL, data = PARAMS)
    print(r.text)

def SaveToFile(filename, content):
    with open("D:\\pyquests\\src\\dls\\"+filename+".jpg", "wb") as handle:
        for data in tqdm(content.iter_content()):
            handle.write(data)

def RedditTitles():
    reddit = p.Reddit(client_id='yd5bYoeRUp7Gfg',client_secret='WWLeGwXepDBVvFYucp6Y4x6hMO8',user_agent='myagent')
    print(reddit.read_only)
    
    for submission in reddit.subreddit('hmmm').hot(limit=50):
        
        url = submission.url
        print(submission.url)
        #response = requests.get(url, stream=True)
        #SaveToFile(str(submission),response)
        
#TEST()
ZrobDemota()


