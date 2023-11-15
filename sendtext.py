import pywhatkit
import pyautogui
import time
import keyboard as k

phoneNumber = input("Enter Phone Number(format +1XXXXXXXXXX)? ")
interval = int(input("How often (intervals in minutes) do you want to them? "))
count = int(input("Number of times you wanna text them? "))
hour = int(input("When do you want to send text (hours 24 hr)? "))
minute = int(input("What minute you want to send the text? "))
message = input("Enter message: ")

try:

    for i in range (0,count):
        pywhatkit.sendwhatmsg(phoneNumber, message, hour, minute)
        pyautogui.click(1050, 950)
        k.press_and_release('enter')

        newMinute = minute+interval
        if(newMinute > 60):
            minute = newMinute - 60
            hour+=1
        else:
            minute = newMinute        

    print("Successfully Sent!")


except:
    print("Error sending message")