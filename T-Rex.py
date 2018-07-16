import pyautogui as m
import numpy as np

size = m.size()

#Coordinates adjusted for macOS (High Sierra)
x = 0.38125*size[0]
y = 0.2934*size[1]

stdpath = m.screenshot(region=(x,y, 100, 2))
m.moveTo(x,y)
constant = np.array(stdpath)
while True:
    tree = m.screenshot(region=(x,y, 100, 2))
    ar = np.array(tree)
    if (ar!=constant).any():
        m.press('space')
