file = open("day3input.txt", "r")
somme = 0
lines = file.readlines()
file.close()
lines = [line[0:-1].replace(" ", "") for line in lines]

n = len(lines)

def digit(carac):
	return carac in "0123456789"
def condition(k, p):
	return not(digit(lines[k][p])) and lines[k][p] != '.'

nombre = ""
cond = False

for i in range(n):
	l = len(lines[i])
	for j in range(l):
		if digit(lines[i][j]):
			nombre += lines[i][j]
			if j-1 >= 0 and condition(i, j-1): cond = True
			if j+1 <= l-1 and condition(i, j+1): cond = True

			if i >= 1:
				if condition(i-1,j): cond = True
				if j-1 >= 0 and condition(i-1,j-1): cond = True
				if j+1 <= l-1 and condition(i-1, j+1): cond = True
		
			if i+1 <= n-1:
				if condition(i+1,j):cond = True
				if j-1 >= 0 and condition(i+1, j-1): cond = True
				if j+1 <= l-1 and condition(i+1, j+1): cond = True
		else:
			if cond:
				somme += int(nombre)
				cond = False
			nombre = ""
	if cond: 
		somme += int(nombre)
		cond = False
	nombre = ""
print(somme)