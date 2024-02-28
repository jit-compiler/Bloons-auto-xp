from pyautogui import *
import pyautogui
import time
import keyboard
import random
from game.game import Game
from pynput.keyboard import Controller

UPGRADE_1 = (328, 477)
UPGRADE_2 = (328, 629)
UPGRADE_3 = (328, 777)

keyboard = Controller()

def placeCustomMonkeys():
    SUB_1 = (1227, 175)
    pyautogui.moveTo(SUB_1)
    keyboard.press('x')
    keyboard.release('x')
    time.sleep(0.3)
    pyautogui.click(SUB_1)
    pyautogui.click(SUB_1)
    time.sleep(0.3)
    pyautogui.moveTo(UPGRADE_1)
    pyautogui.click(UPGRADE_1)
    pyautogui.click(UPGRADE_1)
    time.sleep(0.3)
    pyautogui.moveTo(UPGRADE_3)
    pyautogui.click(UPGRADE_3)
    pyautogui.click(UPGRADE_3)
    pyautogui.click(UPGRADE_3)
    pyautogui.click(UPGRADE_3)
    time.sleep(3)
    

def main():
   time.sleep(2)
   Game.clickPlay()
   Game.clickExpertMaps()
   Game.clickInfernalMap()
   Game.clickEasy()
   Game.clickDeflation()
   Game.clickOK()
   Game.setupMonkeys()
   placeCustomMonkeys()
   Game.startAndSpeedUp()
   Game.clickNextAndHome()
   main()

    # time.sleep(2)  # wait for 2 seconds before pressing the key
    # keyboard.press('f')
    # keyboard.release('f')

if __name__ == "__main__":
    main()
    
    # 288 858