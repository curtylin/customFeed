import json
import requests     #remember to import requests https://www.dataquest.io/blog/python-api-tutorial/

outputFileName = 'tweetOutputs.txt'
outputFile = open(outputFileName, 'w')

twitterUser = cnnbrk
numberOfTweets = 5

HTTPRequest = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + twitterUser + '&count=' + numberOfTweets + '&exclude_replies=true'
tweets = json.load(requests.get(HTTPRequest))

for tweet in tweets:
    tweetTime = tweet["created_at"]
    tweetText = tweet["text"]
    tweetUser = tweet["user"]
    userName = tweetUser["screen_name"]
    outputLine = tweetTime + "\t@" + userName + "\t" + tweetText "\n"
    outputFile.write(outputLine)

outputFile.close
