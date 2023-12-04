file = open("day4input.txt", "r")
lines = file.readlines()
file.close()
points = 0
for line in lines:
	l = line.split(":")[1].split("|")
	
	# Possible winning numbers
	w = l[0]
	n = l[1]
	nombre = ""
	numbers = []
	winning = 0

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

	if winning >= 1:
		print(winning)
		result = 2**(winning-1)
		print(result)
		points += result

print(points)