# FTX Dogecoin bot powered by Elon Musk on Twitter 

FTX-ELON-TWITTER-DOGE-BOT is a python script which monitor Elon Musk twitter feed for "Dogecoin" keywords.

*Be aware that this script is for educational purposes only, by an idea of antoinebaron-io*

The script will open a stream connection to twitter API and monitor Elon Musk twitter account.
If a mention of dogecoin is found in his last tweet, the script will immediately request a convert order to $DOGE from your $USD balance and automatically convert it back to $USD after 15 minutes.

The script will also writed down in a Gsheet document every action so you know how much USD you made at the end of the convert process.


## Dependencies

- API key from your FTX account (https://ftx.com/referrals#a=3168006) Get 5% Fees off with my referral link :)
- API key from twitter developer (https://developer.twitter.com/en/apply-for-access)
- Google Gsheet API and service_account created with JSON creds (https://developers.google.com/workspace/guides/create-project)

The script works using : 
- Tweepy : https://docs.tweepy.org/en/stable/
- Gspread : https://docs.gspread.org/en/latest/
- FTX API : https://docs.ftx.com/#overview

## Installation

>pip3 install tweepy, gspread, requests, python-decouple

## Configuration

You have to store your Twitter and FTX API credentials into the .dev file and download your Google service_account.json file.

## Usage

>python3.8 ./twitter_stream.py

----------------------------------------------------------------------------------------
newkkfnepy