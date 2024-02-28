from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os.path
import pyscreeze

class Game:
    @staticmethod
    def clickPlay():
        try:
        # Check screen resolution and set image path accordingly
            image_path = "./pictures/play.png"

        # Check if the image file exists
            if not os.path.isfile(image_path):
                raise Exception(f"Error: Image file '{image_path}' not found.")

        # Keep trying to start the battle until successful
            while True:
                result = pyautogui.locateOnScreen(image_path, confidence=0.9)
                if result is not None:
                    print("Play image found. Clicking...")
                    x, y = pyautogui.center(result)
                    pyautogui.moveTo(x, y)
                    pyautogui.click()
                    time.sleep(1)
                    break
                else:
                    print("Battle image not found. Retrying...")
                    time.sleep(1)  # Wait for a bit before retrying to avoid overloading the CPU
        except Exception as e:
            time.sleep(1)
            Game.startBattle()
            
    @staticmethod
    def clickExpertMaps():
        try:
        # Check screen resolution and set image path accordingly
            image_path = "./pictures/expertMaps.png"

        # Check if the image file exists
            if not os.path.isfile(image_path):
                raise Exception(f"Error: Image file '{image_path}' not found.")

        # Keep trying to start the battle until successful
            while True:
                result = pyautogui.locateOnScreen(image_path, confidence=0.9)
                if result is not None:
                    print("Advanced Maps image found. Clicking...")
                    battle_x, battle_y = pyautogui.center(result)
                    pyautogui.moveTo(battle_x, battle_y)
                    pyautogui.click()
                    time.sleep(1)
                    break
                else:
                    print("Battle image not found. Retrying...")
                    time.sleep(1)  # Wait for a bit before retrying to avoid overloading the CPU
        except Exception as e:
            time.sleep(1)
            Game.startBattle()
            

    @staticmethod
    def clickInfernalMap():
        try:
            x = 1278
            y = 562
            color = (69, 25, 0)
            time.sleep(1)

            # while not pyautogui.pixelMatchesColor(x, y, color):
            #     time.sleep(0.1)
        
            pyautogui.click(x, y)
            print("Clicked the specified coordinates.")
        except Exception as e:
            print("Error: " + str(e))
            
    @staticmethod
    def clickEasy():
        try:
            x = 618
            y = 386
            time.sleep(1)

            # while not pyautogui.pixelMatchesColor(x, y, color):
            #     time.sleep(0.1)
        
            pyautogui.click(x, y)
            print("Clicked the specified coordinates.")
        except Exception as e:
            print("Error: " + str(e))

    @staticmethod
    def clickDeflation():
        try:
            x = 1280
            y = 447
            time.sleep(1)

            # while not pyautogui.pixelMatchesColor(x, y, color):
            #     time.sleep(0.1)
        
            pyautogui.click(x, y)
            print("Clicked the specified coordinates.")
        except Exception as e:
            print("Error: " + str(e))
            
    @staticmethod
    def clickOK():
        try:
            x = 951
            y = 757
            time.sleep(5)

            # while not pyautogui.pixelMatchesColor(x, y, color):
            #     time.sleep(0.1)
        
            pyautogui.click(x, y)
            print("Clicked the specified coordinates.")
        except Exception as e:
            print("Error: " + str(e))
            
    @staticmethod
    def setupMonkeys():
        try:
            VILLAGE_X = 1581
            VILLAGE_Y = 497
            SNIPER_X = 1514
            SNIPER_Y = 564
            ALCHEMIST_X = 1585
            ALCHEMIST_Y = 611
            
            UPGRADE_1 = (328, 477)
            UPGRADE_2 = (328, 629)
            UPGRADE_3 = (328, 777)
            
            
            
            # PLACE MONKEYS
            time.sleep(1)
            pyautogui.moveTo(VILLAGE_X, VILLAGE_Y)
            keyboard.press('k')
            keyboard.release('k')
            time.sleep(0.3)
            pyautogui.click(VILLAGE_X, VILLAGE_Y)
            time.sleep(0.3)
            pyautogui.moveTo(SNIPER_X, SNIPER_Y)
            keyboard.press('z')
            keyboard.release('z')
            time.sleep(0.3)
            pyautogui.click(SNIPER_X, SNIPER_Y)
            time.sleep(0.3)
            pyautogui.moveTo(ALCHEMIST_X, ALCHEMIST_Y)
            keyboard.press('f')
            keyboard.release('f')
            time.sleep(0.3)
            pyautogui.click(ALCHEMIST_X, ALCHEMIST_Y)
            
            # UPGRADE MONKEYS
            # village
            time.sleep(0.3)
            pyautogui.moveTo(VILLAGE_X, VILLAGE_Y)
            pyautogui.click(VILLAGE_X, VILLAGE_Y)
            time.sleep(0.3)
            pyautogui.moveTo(UPGRADE_1)
            pyautogui.click(UPGRADE_1)
            pyautogui.click(UPGRADE_1)
            time.sleep(0.3)
            pyautogui.moveTo(UPGRADE_3)
            pyautogui.click(UPGRADE_3)
            pyautogui.click(UPGRADE_3)
            
            # sniper
            time.sleep(0.3)
            pyautogui.moveTo(SNIPER_X, SNIPER_Y)
            pyautogui.click(SNIPER_X, SNIPER_Y)
            time.sleep(0.3)
            pyautogui.moveTo(UPGRADE_2)
            pyautogui.click(UPGRADE_2)
            pyautogui.click(UPGRADE_2)
            time.sleep(0.3)
            pyautogui.moveTo(UPGRADE_3)
            pyautogui.click(UPGRADE_3)
            pyautogui.click(UPGRADE_3)
            pyautogui.click(UPGRADE_3)
            pyautogui.click(UPGRADE_3)
            
            # alchemist
            
            time.sleep(0.3)
            pyautogui.moveTo(ALCHEMIST_X, ALCHEMIST_Y)
            pyautogui.click(ALCHEMIST_X, ALCHEMIST_Y)
            time.sleep(0.3)
            pyautogui.moveTo(UPGRADE_1)
            pyautogui.click(UPGRADE_1)
            pyautogui.click(UPGRADE_1)
            pyautogui.click(UPGRADE_1)
            pyautogui.click(UPGRADE_1)
            
        except Exception as e:
            print("Error: " + str(e))
            
    @staticmethod
    def startAndSpeedUp():
        COORDINATES = (1822, 1012)
        pyautogui.moveTo(COORDINATES)
        pyautogui.click(COORDINATES)
        pyautogui.click(COORDINATES)
        
        # hide upgrade menu
            
        time.sleep(0.3)
        pyautogui.moveTo(1000, 500)
        pyautogui.click(1000, 500)
        
    @staticmethod
    def clickNextAndHome():
        try:
        # Check screen resolution and set image path accordingly
            image_path = "./pictures/next.png"

        # Check if the image file exists
            if not os.path.isfile(image_path):
                raise Exception(f"Error: Image file '{image_path}' not found.")

        # Keep trying to start the battle until successful
            while True:
                result = pyautogui.locateOnScreen(image_path, confidence=0.9)
                if result is not None:
                    print("Play image found. Clicking...")
                    x, y = pyautogui.center(result)
                    pyautogui.moveTo(x, y)
                    pyautogui.click()
                    time.sleep(1)
                    break
                else:
                    print("Battle image not found. Retrying...")
                    time.sleep(1)  # Wait for a bit before retrying to avoid overloading the CPU
                    
            image_path = "./pictures/home.png"

        # Check if the image file exists
            if not os.path.isfile(image_path):
                raise Exception(f"Error: Image file '{image_path}' not found.")

        # Keep trying to start the battle until successful
            while True:
                result = pyautogui.locateOnScreen(image_path, confidence=0.9)
                if result is not None:
                    print("Play image found. Clicking...")
                    x, y = pyautogui.center(result)
                    pyautogui.moveTo(x, y)
                    pyautogui.click()
                    time.sleep(1)
                    break
                else:
                    print("Home image not found. Retrying...")
                    time.sleep(1)  # Wait for a bit before retrying to avoid overloading the CPU
        except Exception as e:
            time.sleep(1)
            Game.startBattle()