file = open("day1input.txt", 'r')
lines = file.readlines()
somme = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
n = len(numbers)
for line in lines:
	digits = []
	l = len(line)
	for i in range(0, l, 1):
		if line[i].isdigit():
			digits.append(int(line[i]))
		else:
			for j in range(i+1, l, 1):
				texte = line[i:j]
				for k in range(n):
					if texte == numbers[k]:
						digits.append(k+1)
						i = j
	nombre = 0
	if len(digits) == 1:
		nombre = digits[0]*11
	else:
		nombre = digits[0]*10 + digits[-1]
	somme += nombre

print(somme)
file.close()