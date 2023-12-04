file = open("day4input.txt", "r")
lines = file.readlines()
file.close()
scratchcards = [1 for _ in range(len(lines))]
ncard = 0
numberScratchcards = 0
for line in lines:
	l = line.split(":")[1].split("|")
	ncard += 1
	# Possible winning numbers
	w = l[0]
	n = l[1]
	nombre = ""
	numbers = []
	winning = 0
	numberScratchcards += scratchcards[ncard-1]
	for c in range(len(n)):
		if n[c].isdigit():
			nombre += n[c]
		else:
			if nombre != "":
				numbers.append(int(nombre))
				nombre = ""
	nombre = ""
	for c in range(len(w)):
		if w[c].isdigit():
			nombre += w[c]
		else:
			if nombre != "":
				if int(nombre) in numbers:
					winning += 1
			nombre = ""
	if nombre != "":
		if int(nombre) in numbers:
			winning += 1

	for k in range(scratchcards[ncard-1]):
		if winning >= 1:
			for j in range(winning):
				scratchcards[ncard+j] += 1

print(numberScratchcards)