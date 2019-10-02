from gpiozero import LED
from time import sleep

led = LED(17)

word = input("input here: ").lower()

def dot():
	print("dot")		
	led.on()
	sleep(.5)

def dash():
	print("dash")		
	led.on()
	sleep(1.5)

def dotSpace():		
	led.off()
	sleep(.5)

def letterSpace():
	print("Space")		
	led.off()
	sleep(1.5)

def wordSpace():
	print("\n-----------------SPACE----------\n")		
	led.off()
	sleep(3.5)

for i in word:
	while i == "a":
		print("-------------------A")
		dot()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "b":
		print("-------------------B")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "c":
		print("-------------------C")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "d":
		print("-------------------D")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "e":
		print("-------------------E")
		dot()
		letterSpace()
		break

	while i == "f":
		print("-------------------F")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "g":
		print("-------------------G")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "h":
		print("-------------------H")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "i":
		print("-------------------I")
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "j":
		print("-------------------J")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "k":
		print("-------------------K")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		letterSpace()
		break
	
	while i == "l":
		print("-------------------L")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "m":
		print("-------------------M")
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "n":
		print("-------------------N")
		dash()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "o":
		print("-------------------O")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "p":
		print("-------------------P")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "q":
		print("-------------------Q")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "r":
		print("-------------------R")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dot()
		letterSpace()
		break	

	while i == "s":
		print("-------------------S")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "t":
		print("-------------------T")
		dash()
		letterSpace()
		break	

	while i == "u":
		print("-------------------U")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "v":
		print("-------------------V")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "w":
		print("-------------------W")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "x":
		print("-------------------X")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "y":
		print("-------------------Y")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "z":
		print("-------------------Z")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break	

	while i == " ":
		wordSpace()
		break

	while i == "0":
		print("-------------------0")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "1":
		print("-------------------1")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "2":
		print("-------------------2")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break
	
	while i == "3":
		print("-------------------3")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break
	
	while i == "4":
		print("-------------------4")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "5":
		print("-------------------5")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "6":
		print("-------------------6")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "7":
		print("-------------------7")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "8":
		print("-------------------8")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "9":
		print("-------------------9")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == ".":
		print("-------------------period")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == ",":
		print("-------------------comma")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == "?":
		print("-------------------?")
		dot()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "!":
		print("-------------------Exclamation")
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		letterSpace()
		break

	while i == ":":
		print("-------------------:")
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		dotSpace()
		dot()
		dotSpace()
		dot()
		letterSpace()
		break

	while i == "'":
		print("-------------------Apostrophe")
		dot()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dash()
		dotSpace()
		dot()
		letterSpace()
		break	
