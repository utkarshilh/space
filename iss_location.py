import requests 
import json 
import time 
from  datetime import   datetime 

import os 

import csv 






# creating output.csv file if not exits

if not os.path.exists("output.csv"):
    with open("output.csv","w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["latitude","longitude","timestamp"])

    print("file created successfully.") 

else :
    print("files alreaty exists")







url = "http://api.open-notify.org/iss-now.json"

# print("Tracking ISS location (press CTRL+C to stop)...")

# while True :
response = requests.get(url) 
data = response.json()

position = data["iss_position"]

latitude = position["latitude"]

longitude = position["longitude"]

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("output.csv","a", newline= '') as f:
    writer = csv.writer(f)
    writer.writerow([latitude,longitude,timestamp])



print(f"ISS Current Location -> Latitude : {latitude} , Longitude : {longitude} at {timestamp}")




