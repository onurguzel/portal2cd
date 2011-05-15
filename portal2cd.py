#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import os
import tweepy

delta = datetime.datetime(2011,4,20)-datetime.datetime.now()

# Consumer keys for your twitter application
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# Access tokens for ypur twitter account
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Tweet
api = tweepy.API(auth)
if delta.days > 0:
    if delta.days == 1:
        message = "Portal 2 launchs today! #portal2 - http://goo.gl/8YFQ4"
    else:
        message = "Portal 2 will be launched after %d days #portal2 - http://www.thinkwithportals.com/" % delta.days
    api.update_status(message)
else:
    if not os.path.exists("launched"):
        api.update_status("Portal 2 has launched #portal2 - http://store.steampowered.com/app/620/")
        open("launched", "w").write("")
