tweet = "maintenance test https://t.co/y8Ckfsn3Ub uwu"
if "https://t.co" in tweet:
    temp = tweet.split("https://t.co")
    print(temp)
    tweet.replace("https://t.co", "")
    print(tweet)
else:
    print("Kagak ada")

print(tweet)

sss = "https://ton.twitter.com/1.1/ton/data/dm/1219983622142218244/1219983611962638336/hMqlXHC_.jpg"
arr = sss.split('/')
print(arr[len(arr)-1])
