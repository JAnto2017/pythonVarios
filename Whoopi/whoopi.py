Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> import random
>>> from time import sleep
>>> from gpiozero import Button
>>> button = Button(2)
>>> trumps = ['ben-fart.wav','ca-fart.wav','marc-fart.wav']
>>> while True:
	button.wait_for_press()
	parp = random.choice(trumps)
	os.system("aplay {0}".format(parp))
	sleep(2)
