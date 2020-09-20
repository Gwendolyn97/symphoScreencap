import os
import random
import time
import tweepy

from dotenv import load_dotenv
load_dotenv()
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_secret = os.getenv("access_secret")

def twitter():  #returns api so that i dont have to copy and paste this in every fucking bit i want to use the twitter api 
                #like holy fucking shit there has to be an easier way to do thi 78y6juhigtbn
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    return api

directory = "D:\\Symphogear"

while len(os.listdir(f"{directory}")) != 0:
    try: 
        image = random.choice(os.listdir(f"{directory}"))
        print(f"{image} has been selected.")

        twitter().update_with_media(filename = f"{directory}\\{image}", status = f"{image}")
        print(f"{image} has been sent!")
        
        os.remove(f"{directory}\\{image}")
        print(f"Image has been deleted.\nThere are {len(os.listdir(directory))} images left in {directory}")
        
        print(f"Task completed. Standing by for 600 seconds.\n-----")
        time.sleep(600)    
    except tweepy.TweepError as e: 
        print(f"Exception raised!\nCode: {e.api_code}\nReason: {e.reason}")
    
        if e.reason == "File is too big, must be less than 3072kb.":
            print(f"{image} is too large to upload. Deleting!")
            os.remove(f"{directory}\\{image}")
            print(f"There are {len(os.listdir(directory))} images left in {directory}")
    finally: 
        pass
else:
    print(f"{directory} is empty.")

