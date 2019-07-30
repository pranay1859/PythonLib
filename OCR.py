import pytesseract
from PIL import Image
import time


def scanEng(pic):
	img = Image.open(pic)
	text = pytesseract.image_to_string(img)
	time.sleep(1)
	print(text)

def scanThai(pic):
	img = Image.open(pic)
	text = pytesseract.image_to_string(img,lang='tha')#thai 
	time.sleep(1)
	print(text)

scanEng("book2.jpg")

# result
"""
- v 7

Things don�t always go according to plan. Here are some common problems
and how you can try to solve them:

1/ No lights on your Raspberry Pi: This can happen if you forgot to con-
nect the micro USB power connector or if the power supply isn't capable
of supplying your Raspberry Pi with enough power. Check that it�s rated
to at least 5V 700mA (3.5 watts).

1/ Only the red light comes on: Your Raspberry Pi has power. but it can�t
read the operating system on your SD card. First, make sure your SD
card is firmly inserted. Then check that you've correctly created the
disk image. If that doesn�t work, you can try testing your SD card on
another Raspberry Pi to see if you get the same problem. if all else fails,
try using a pre-imaged SD card.

1/ No output on the monitor: Check your monitor connection and your
monitor's power connection. Make sure that your monitor is turned on.
(Sounds silly. but we�ve all done this at least once!) Then check that
your monitor is using the correct input source. Use a button on the
front of the monitor to cycle through them or use the monitor's remote
control.

1/ Inconsistent behavior or hang-ups: Your Raspberry Pi uses power at
different amounts depending on what it�s doing. Make sure you have a
good power supply and that it isn't overtaxed.

[Finished in 4.2s]

"""
