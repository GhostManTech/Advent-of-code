file = open("day2input.txt", "r")

lines = file.readlines()
games = []
sumPower = 0

for line in lines:
	line2 = line.split(":")[1][0:-1]
	hands = line2.split(";")
	cond = True
	maxred, maxblue, maxgreen = 0,0,0
	for h in hands:

		colors = h.split(",")
		for color in colors:
			c = color[1:]

			number = ""
			i = 0
			while c[i].isdigit():
				number += c[i]
				i += 1
			number = int(number)
			
			if (c.endswith("red") and number > maxred):maxred = number
			if (c.endswith("blue") and number > maxblue):maxblue = number
			if (c.endswith("green") and number > maxgreen):maxgreen = number

	sumPower += maxred*maxblue*maxgreen

print(sumPower)