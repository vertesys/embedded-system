from PIL import Image, ImageDraw, ImageFont

from lib_tft24T import TFT24T
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import spidev
from time import sleep

# Raspberry Pi configuration.
#For LCD TFT SCREEN:


    # # Alternatively can clear to a black screen by simply calling:
    # TFT.clear()
    # print('Loading image...')
    # image = Image.open('balloon.jpg')
    #
    # # Resize the image and rotate it so it's 240x320 pixels.
    # image = image.rotate(90,0,1).resize((240, 320))
    # # Draw the image on the display hardware.
    # print('Drawing image')
    # TFT.display(image)
    #
    # text1 = \
    #         """VIRTUS NEUTRINO"""
    #
    # # TFT.clear()
    # print ("show a font in giant letters")
    #
    # ###############################################""
    #
    # text = u'toto 123456.'
    # text2 = u'toto nnnn.'
    # font = ImageFont.truetype('Pillow/Tests/fonts/DejaVuSansMono.ttf', 30)
    #
    # image2 = Image.new('RGBA', (240, 320))
    # image2 = Image.open('balloon.jpg')
    # draw2 = ImageDraw.Draw(image2)
    # draw2.text((10, 25), text=text, font=font)
    # draw2.text((10, 70), text=text2, font=font, fill="RED")
    #
    # # image2 = image2.rotate(90, expand=1)
    # image2 = image2.rotate(90, 0, 2).resize((240, 320))
    #
    # TFT.display(image2)
    #
    # sleep(3)

class Ecran():

    def __init__(self):
        DC = 24
        RST = 25
        LED = 12

        # Create TFT LCD/TOUCH object:
        self.TFT = TFT24T(spidev.SpiDev(), GPIO, landscape=False)
        # Initialize display.
        self.TFT.initLCD(DC, RST, LED)
        # Get the PIL Draw object to start drawing on the display buffer.
        draw = self.TFT.draw()
        self.TFT.clear((0, 0, 0))

    def image(self,image : str):
        # self.TFT.clear()
        image = Image.open(image)
        # Resize the image and rotate it so it's 240x320 pixels.
        image = image.rotate(90,0,1).resize((240, 320))
        # Draw the image on the display hardware.
        self.TFT.display(image)

    def text(self,text:object):

        tabtext =text.split()
        if len(tabtext) == 1:
            font = ImageFont.truetype('Pillow/Tests/fonts/DejaVuSansMono.ttf', 30)
            image2 = Image.new('RGBA', (240, 320))
            draw2 = ImageDraw.Draw(image2)
            draw2.text((10, 25), text=text, font=font)

            # image2 = image2.rotate(90, expand=1)
            image2 = image2.rotate(90, 0, 2).resize((240, 320))
            self.TFT.display(image2)
        else:
            font = ImageFont.truetype('Pillow/Tests/fonts/DejaVuSansMono.ttf', 30)
            image2 = Image.new('RGBA', (240, 320))
            draw2 = ImageDraw.Draw(image2)
            position = 25
            for i in tabtext:
                draw2.text((10, position), text=i, font=font)
                position = position + 40
            image2 = image2.rotate(90, 0, 2).resize((240, 320))
            self.TFT.display(image2)






#
#
#
# virtus = Ecran()
#
# virtus.text('sylvain besseron de toulon')
