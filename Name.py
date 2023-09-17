from ast import keyword
from tkinter import*
import tkinter.font
from gpiozero import LED
import time
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

root = Tk()
root.title("Morse Code into name")
root.geometry("280x170")
myFont = tkinter.font.Font(family = 'Helvetica' , size = 10, weight = 'bold')
led = LED(17)

def dot():
	led.on()
	time.sleep(0.5)
	led.off()
	time.sleep(0.5)
	print("Dot")

def dash():
	led.on()
	time.sleep(1)
	led.off()
	time.sleep(0.5)
	print("Dash")

def exit():
	root.destroy()

def MorseCode():
	text = Text_Box.get('1.0','end-1c')
	if len(text)>12 or len(text) < 0:
		led.off()
		print("Please enter a name within word limit")
		print("word limit - 12")
		return
	else:
		print("Calculating morse code..")
		time.sleep(1)
	
	for keyword in text:
		if keyword.lower() == 'a':
			dot()
			dash()
		elif keyword.lower() == 'b':
			dash()
			dot()
			dot()
			dot()
		elif keyword.lower() == 'c':
			dash()
			dot()
			dash()
			dot()
		elif keyword.lower() == 'd':
			dash()
			dot()
			dot()
		elif keyword.lower() == 'e':
			dot()
		elif keyword.lower() == 'f':
			dot()
			dot()
			dash()
			dot()
		elif keyword.lower() == 'g':
			dash()
			dash()
			dot()
		elif keyword.lower() == 'h':
			dot()
			dot()
			dot()
			dot()
		elif keyword.lower() == 'i':
			dot()
			dot()
		elif keyword.lower() == 'j':
			dot()
			dash()
			dash()
			dash()
		elif keyword.lower() == 'k':
			dash()
			dot()
			dash()
		elif keyword.lower() == 'l':
			dot()
			dash()
			dot()
			dot()
		elif keyword.lower() == 'm':
			dash()
			dash()
		elif keyword.lower() == 'n':
			dash()
			dot()
		elif keyword.lower() == 'o':
			dash()
			dash()
			dash()
		elif keyword.lower() == 'p':
			dot()
			dash()
			dash()
			dot()
		elif keyword.lower() == 'q':
			dash()
			dash()
			dot()
			dash()
		elif keyword.lower() == 'r':
			dot()
			dash()
			dot()
		elif keyword.lower() == 's':
			dot()
			dot()
			dot()
		elif keyword.lower() == 't':
			dash()
		elif keyword.lower() == 'u':
			dot()
			dot()
			dash()
		elif keyword.lower() == 'v':
			dot()
			dot()
			dot()
			dash()
		elif keyword.lower() == 'w':
			dot()
			dash()
			dash()
		elif keyword.lower() == 'x':
			dash()
			dot()
			dot()
			dash()
		elif keyword.lower() == 'y':
			dash()
			dot()
			dash()
			dash()
		elif keyword.lower() == 'z':
			dash()
			dash()
			dot()
			dot()
Label(root, text='Enter name', bg= 'yellow', font = myFont, height = 1, width = 35).grid(row = 0, column = 1)

Text_Box = Text(root, height = 1, width = 30, bg = 'grey')
Text_Box.grid(row = 1, column = 1, padx = 20, pady = 10)

submitButton = Button(root, text = 'Submit', font = myFont, command = MorseCode, bg = 'white')
submitButton.grid(row = 3, column = 1)

Exit_Button = Button(root, text = 'Exit', font = myFont, command = exit, height = 1, width = 6)
Exit_Button.grid(row = 4, column = 1)

root.mainloop()
