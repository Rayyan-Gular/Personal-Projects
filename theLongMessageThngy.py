import pyperclip, pyautogui, time

time.sleep(5)
pyperclip.copy("meow" * 200)

for i in range(71):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)

pyautogui.typewrite("meow" * 43)
pyautogui.press('enter')
