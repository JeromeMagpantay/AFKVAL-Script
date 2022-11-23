#AFK Script for Valorant.

import pyautogui as pag;
import time;
import random;

while True:
    x_axis = random.randint (500,700);
    y_axis = random.randint (500,700);
    pag.click();
    pag.moveTo(x_axis,y_axis,0.5);
    time.sleep(3);
