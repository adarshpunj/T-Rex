from PIL import Image
import numpy as np
import pyautogui as m
import time
stdpath = m.screenshot(region=(549,264, 100, 2))
m.moveTo(549,264)
constant = np.array(stdpath)
while True:
    tree = m.screenshot(region=(549,264, 100, 2))
    ar = np.array(tree)
    if (ar!=constant).any():
        m.press('space') 
