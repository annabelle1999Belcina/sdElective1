from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(5, 6, 12, 16, 13, 19, 20, 21)



pattern = {
	 0:(0, 1, 1, 1, 1, 1, 1, 0),
	 1:(0, 0, 0, 1, 0, 0, 1, 0),
	 2:(1, 0, 1, 1, 1, 1, 0, 0),
	 3:(1, 0, 1, 1, 0, 1, 1, 0),
	 4:(1, 1, 0, 1, 0, 0, 1, 0),
	 5:(1, 1, 1, 0, 0, 1, 1, 0),
	 6:(1, 1, 1, 0, 1, 1, 1, 0),
	 7:(0, 1, 1, 1, 0, 0, 1, 0),
	 8:(1, 1, 1, 1, 1, 1, 1, 0),
	 9:(1, 1, 1, 1, 0, 1, 1, 0)
}

n = int(input("enter number: "))

def ones(num):
	leds.value = num
def tens(num):
	number  = list(num)
	number[7] = 1
	num = tuple(number)
	leds.value = num
	sleep(0.5)

for i in range(n,-1,-1):
	if n >=10:
		tens(pattern[int(str(n)[0])])
		ones(pattern[int(str(n)[1])])
		sleep(0.5)
		n-=1
	else:
		ones(pattern[int(str(n)[0])])
		sleep(1)
		n-=1

			
	    	




