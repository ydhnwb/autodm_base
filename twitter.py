import tweepy
import constants
import time
import _json
from requests_oauthlib import OAuth1
import requests
import os

class Twitter:
    def __init__(self):
        print("initializing twitter....")
        self.inits = tweepy.OAuthHandler(constants.CONSUMER_KEY, constants.CONSUMER_SCRET)
        self.inits.set_access_token(constants.ACCESS_KEY, constants.ACCESS_SECRET)
        self.api = tweepy.API(self.inits)


    def read_dm(self):
        print("Get direct messages...")
        dms = list()
        try:
            api = self.api
            dm = api.list_direct_messages()
            for x in range(len(dm)):
                sender_id = dm[x].message_create['sender_id']
                message = dm[x].message_create['message_data']['text']
                message_data = str(dm[x].message_create['message_data'])
                json_data = _json.encode_basestring(message_data)
                print(json_data)
                print("Getting message -> "+str(message)+" by sender id "+str(sender_id))

                if "attachment" not in json_data:
                    print("Dm does not have any media...")
                    d = dict(message=message, sender_id=sender_id, id=dm[x].id, media = None, shorted_media_url = None)
                    dms.append(d)
                    dms.reverse()

                else:
                    print("Dm have an attachment..")
                    attachment = dm[x].message_create['message_data']['attachment']
                    d = dict(message=message, sender_id=sender_id, id=dm[x].id, media = attachment['media']['media_url'], shorted_media_url = attachment['media']['url'])
                    dms.append(d)
                    dms.reverse()

            print(str(len(dms)) + " collected")
            time.sleep(60)
            return dms

        except Exception as ex:
            print(ex)
            time.sleep(60)
            pass


    def delete_dm(self, id):
        print("Deleting dm with id = "+ str(id))
        try:
            self.api.destroy_direct_message(id)
            time.sleep(40)
        except Exception as ex:
            print(ex)
            time.sleep(40)
            pass


    def post_tweet(self, tweet):
        try:
            self.api.update_status(tweet)
        except Exception as e:
            print(e)
            pass

    def post_tweet_with_media(self, tweet, media_url, shorted_media_url):
        try:
            print("shorted url" + shorted_media_url)
            print("Downloading media...")
            arr = str(media_url).split('/')
            auth = OAuth1(client_key= constants.CONSUMER_KEY,
                          client_secret= constants.CONSUMER_SCRET,
                          resource_owner_secret= constants.ACCESS_SECRET,
                          resource_owner_key= constants.ACCESS_KEY)
            r = requests.get(media_url, auth = auth)
            with open(arr[len(arr)-1], 'wb') as f:
                f.write(r.content)

            print("Media downloaded successfully!")
            if shorted_media_url in tweet:
                tweet = tweet.replace(shorted_media_url, "")
            else:
                print("kagak ada")

            self.api.update_with_media(filename= arr[len(arr)-1], status = tweet)
            os.remove(arr[len(arr)-1])
            print("Upload with media success!")
        except Exception as e:
            print(e)
            pass
