import pyautogui
import time

# Wait before starting (so you can focus the input field)
time.sleep(5)

while True:
    # Open the file correctly in read mode
    with open("C:/Users/USER/Desktop/spambot/1.txt", "r") as f:
        # Loop through each line and send it
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            time.sleep(0.5)  # delay between lines (optional)

    time.sleep(3)  # wait before repeating the whole file (adjust as needed)












