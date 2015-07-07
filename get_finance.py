import logging
import os
import sys

from PIL import Image, ImageDraw, ImageFont
from twython import Twython
from yahoo_finance import Share

logger = logging.getLogger(__name__)

APP_KEY = os.environ.get('APP_KEY')
APP_SECRET = os.environ.get('APP_SECRET')
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def main(argv):
    if len(argv) == 1:
        print('Not enough arguments')
        return

    for symbol in argv[1:]:
        print(symbol)
        stock = Share(symbol)
        if stock.data_set['Name']:
            print(stock.data_set['Name'])
            print(stock.data_set)
            img = Image.open('keep-calm-and-carry-on.png')
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('Aaargh.ttf', 20)
            draw.text((0, 0), stock.data_set['Name'], (255, 255, 255), font=font)
            draw.text((0, 30), stock.data_set['LastTradePriceOnly'], (255, 255, 255), font=font)
            draw.text((0, 60), '{} {}'.format(stock.data_set['LastTradeDate'], stock.data_set['LastTradeTime']), (255, 255, 255), font=font)
            img.save('output/{}.png'.format(symbol))

            # img = open('output/{}.png'.format(symbol), 'rb')
            twitter.update_status_with_media(status='Checkout this cool image! ${}'.format(symbol), media=img)

if __name__ == "__main__":
    main(sys.argv)
