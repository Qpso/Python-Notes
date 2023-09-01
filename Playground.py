import pyautogui
import subprocess
import time
import pygetwindow as gw
import win32gui
import win32con
import os 

bat_file_path = r'C:\Users\aesas\Desktop\WebPass\launch_webbrowser.bat'

subprocess.run(bat_file_path, shell=True)


# Add a delay before the script starts (you can adjust this value as needed)
time.sleep(1)

def maximize_window_by_title(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# Replace 'WebBrowserPassView' with the actual window title of the application
window_title = 'WebBrowserPassView'

# Launch the application 'WebBrowserPassView.exe' (if not already running) before running this script
# Your code to run the application or perform any other tasks

# Add a delay to allow the application to fully launch (you may need to adjust this value)
time.sleep(0)

# Maximize the window by the window title
maximize_window_by_title(window_title)


# Find the window with the title 'WebBrowserPassView' (exact title or a substring)
web_pass_view_window = gw.getWindowsWithTitle('WebBrowserPassView')[0]

# Activate the 'WebBrowserPassView' window
web_pass_view_window.activate()

# Perform a left click at (x=523, y=146)
pyautogui.moveTo(523, 146)
pyautogui.click()

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 's')

time.sleep(1)

user_profile = os.path.expanduser("~")

# Construct the file path to Desktop\WebPass\
file_path = os.path.join(user_profile, 'Desktop', 'WebPass')

# Copy the file path to the clipboard
pyautogui.write(file_path)

pyautogui.press('enter')

time.sleep(1)

# Move the mouse to (x=445, y=261) and then perform a left click to paste the directory
pyautogui.moveTo(445, 261)
pyautogui.click()

pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')

time.sleep(1)

# Move the mouse to (x=198, y=419) and then perform a left click to write file name
pyautogui.moveTo(198, 419)
pyautogui.click()

pyautogui.write('passwords')

# Move the mouse to (x=504, y=484) and then perform a left click to save the file
pyautogui.moveTo(504, 484)
pyautogui.click()

subprocess.run(["taskkill", "/F", "/IM", "WebBrowserPassView.exe"])

