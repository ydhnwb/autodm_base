# tweet = "maintenance test https://t.co/y8Ckfsn3Ub uwu"
# if "https://t.co" in tweet:
#     temp = tweet.split("https://t.co")
#     print(temp)
#     tweet.replace("https://t.co", "")
#     print(tweet)
# else:
#     print("Kagak ada")
#
# print(tweet)
#
# sss = "https://ton.twitter.com/1.1/ton/data/dm/1219983622142218244/1219983611962638336/hMqlXHC_.jpg"
# arr = sss.split('/')
# print(arr[len(arr)-1])

from twitter import Twitter
# api = Twitter()
# api.post_tweet("Testing gan")
strs = "bfmATURlyecpIkbB4lPco9kWpbh7nLkzTMKXuExRL5w.m3u8?tag=1"
a = strs.find("?tag=1")
b = strs.split("/")
print(a)
print(b[0])
