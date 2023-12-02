file = open("day2input.txt", "r")

lines = file.readlines()
rlimit, glimit, blimit = 12, 13, 14
games = []
k = 1

for line in lines:
	line2 = line.split(":")[1][0:-1]
	hands = line2.split(";")
	cond = True

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
			
			if (c.endswith("red") and number > rlimit) or (c.endswith("blue") and number > blimit) or (c.endswith("green") and number > glimit):
				cond = False
	if cond:games.append(k)
	k += 1

sumGames = sum(games)

print(sumGames)