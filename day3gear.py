file = open("day3input.txt", "r")
somme = 0
lines = file.readlines()
file.close()
lines = [line[0:-1].replace(" ", "") for line in lines]

n = len(lines)

def digit(carac):
	return carac in "0123456789"
def condition(k, p):
	return lines[k][p] == "*"

stars = []
for i in range(n):
	l = len(lines[i])
	for j in range(l):
		if condition(i, j):
			stars.append((i,j))
position = (0,0)
cond = False
nombre = ""

gears = dict()
for element in stars:
	gears[element] = []

for i in range(n):
	l = len(lines[i])
	for j in range(l):
		if digit(lines[i][j]):
			nombre += lines[i][j]
			if j-1 >= 0 and condition(i, j-1) and not(cond):
				position = (i,j-1) 
				cond = True
			if j+1 <= l-1 and condition(i, j+1) and not(cond):
				cond = True
				position = (i,j+1) 
			if i >= 1:
				if condition(i-1,j) and not(cond): 
					cond = True
					position = (i-1, j)
				if j-1 >= 0 and condition(i-1,j-1) and not(cond): 
					cond = True
					position = (i-1, j-1)
				if j+1 <= l-1 and condition(i-1, j+1) and not(cond):
					position = (i-1, j+1)
					cond = True
		
			if i+1 <= n-1:
				if condition(i+1,j) and not(cond):
					cond = True
					position = (i+1, j)
				if j-1 >= 0 and condition(i+1, j-1) and not(cond): 
					cond = True
					position = (i+1, j-1)
				if j+1 <= l-1 and condition(i+1, j+1) and not(cond): 
					cond = True
					position = (i+1, j+1)
		else:
			if cond:
				gears[position].append(int(nombre))
				cond = False
				position = (0,0)
			nombre = ""
	if cond: 
		gears[position].append(int(nombre))
		cond = False
		position = (0,0)
	nombre = ""

for k, v in gears.items():
	if len(v) == 2:
		somme += v[0]*v[1]

print(somme)