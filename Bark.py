#!/bin/python

import twitter
from twitter.models import Status
from bark.ui.ui import TwitterPrompt
from bark.config.config import BarkConfig

class Bark:
    def main(self):
        bark_config = BarkConfig()
        CONSUMER_KEY = bark_config.get_value('API', 'consumer_key')
        CONSUMER_SECRET = bark_config.get_value('API', 'consumer_secret')
        ACCESS_TOKEN = bark_config.get_value('API', 'access_token')
        ACCESS_TOKEN_SECRET = bark_config.get_value('API', 'access_token_secret')
        api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
        tprompt = TwitterPrompt(api)
        tprompt.cmdloop()

if __name__ == '__main__':
    Bark().main()