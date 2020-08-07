import tweepy

from tweepy import Stream
from tweepy import OAuthHandler
import json
import pandas as pd
from pandas import DataFrame as df
import string
import matplotlib.pyplot as plt


#Twitter credentials for the app (deleted for security purposes)
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "TheAn1meMan"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
#for tweet in results:
   # printing the text stored inside the tweet object
   #print ('======================= \n' + tweet.text)
  
#tweetdate = ''
#get tweet ID and date
# for status in api.user_timeline():
#     tweetid = status.id
#     user = api.get_status(tweetid)
#     tweetdate = str(status.created_at)  #date format: yyyy/mm/dd hh:mm:ss
#     dict1= {
#         "ID": tweetid,
#         "year": tweetdate[0:4],
#         "month": tweetdate[6:7],
#         "day": tweetdate[9:10]
#            }
#     with open("tweets.json", "a") as file:
#         json.dump(dict1, file)
#     print("The status was created at : " + tweetdate)

with open("tweets.json", "r") as file:  
    for line in file:
        try:
            data = json.loads(line)            
        except:
            print()
   
    month_count = []
    months = [2, 3, 4, 6, 7]
    count = 0

    for i in months:
        count = 0
        with open("tweets.json", "r") as file:  
            for line in file:
                try:
                    data = json.loads(line) 
                    month_num = int(data['month'])
                    if i == month_num:
                        count += 1           
                except:
                    print()            
            
        month_count.append(count)
               
        

plt.plot(['February', 'March', 'April', 'June', 'July'], month_count)
plt.show()

        
