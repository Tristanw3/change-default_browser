from time import sleep
from pywinauto import Application
import pyautogui

# Open Settings > Default Apps Page
app = Application().start(r"control.exe /name Microsoft.DefaultPrograms /page pageDefaultProgram")
sleep(1.5)

# Open Default browser selection
start_menu_button = pyautogui.locateOnScreen('./auto_images/Chrome_Browser_Button_Image.png', grayscale=True)

start_menu_button_center = pyautogui.center(start_menu_button)
pyautogui.click(start_menu_button_center)

sleep(0.5)
settings_icon = pyautogui.locateOnScreen('./auto_images/Select_Firefox.png', grayscale=True)
settings_icon_center = pyautogui.center(settings_icon)
pyautogui.click(settings_icon_center)
