

import pyautogui
print("\n")
x = int(input("Enter the number of screen shots :- "))
print('*'*33)
for y in range(x):
    images = pyautogui.screenshot('/Users/Syed Mohsin Arif/Desktop'
                                  '/Ammar/ScreenshotTaker/Saved Shots/'
                                  'image'+str(y)+'.png')



