# python into.py
# Basic file for me to play around and learn the sytnax of Python 3 a little

print ('Hello, world!')
print ('They said "HELLO"')
print ('I don\'t think so Bob')
print (r'Here is the path > C:\Path\To\My\Folder')

print ('- - - - - - - - - - - - - - - - -')

x = 'William'
y = "Daly"
z = x + y


print(x)
print(y)
print (z)
print(x + " " + y)

print ('- - - - - - - - - - - - - - - - - - -')

name = "TunaMcFishy"
print (name[0])
print (name[-1])
print (name[1:5])
print (name[:7]) # Chop off until 7th
print (name[2:]) # Chop off 2nd onwards
print (name[:])

print ('- - - - - - - - - - - - - - - - - - -')

word = "asfsafasfsadfdsfafdsafsafdasfqewr"

print(len (word))
print(len (word) , "LOL")
print(word[1])

print ('- - - - - - - - - - - - - - - - - - -')

# Define a list
players = [12 , 45 , 98 , 37 , 82]

# Print particular position
print(players[0])
print(players)

# Set particular position
players[0] = 14
print(players[0])
print(players)

# Add 10 11 and 12 to the end
players = players + [10 , 11 , 12] 
print(players)

# Add 120 to end
players.append(120) 
print(players)

print(players[:2])

# Replace first 2 entries with 0 0
players[:2] = [0,0] 
print(players)

# Delete first 2 entries
players[:2] = [] 
print(players)

# Delete list
players[:] = []
print(players)

print ('- - - - - - - - - - - - - - - - - - -')

age = 27

if age < 27:
	print("lol")

name = "william"

if name is "william":
	print("WILLIAM!")
elif name is "lucy":
	print("FSDFDSFSFSF")
else:
	print("THIS IS AN ELSE")

print ('- - - - - - - - - - - - - - - - - - -')

foods = [ "apple" , "bun" , "egg" , "banana" ]

for f in foods:
	print(f)
	print(len(f))

print ('- - - - - - - - - - - - - - - - - - -')

# 3 times print
for x in range(3):
	print("William Daly is cool")

print ('- - - - - - - - - - - - - - - - - - -')

# From 3 to 10, print 7 times
for x in range(3,10):
	print(x)

print ('- - - - - - - - - - - - - - - - - - -')

# Go from 10 to 40 in steps of 5
for x in range(10,40,5):
	print(x)

print ('- - - - - - - - - - - - - - - - - - -')

buttcrack = 1

while buttcrack < 11:
	print("This is the buttcrack")
	buttcrack+=1
	break

print ('- - - - - - - - - - - - - - - - - - -')

derp = 10

for x in range(99):
	if x == derp:
		print("Now we're breaking out")
		break
	else:
		print("Need to increment again")

print ('- - - - - - - - - - - - - - - - - - -')

numbersTaken = [3,5,7]

# continue means skip past everything but keep iterating in the loop
for b in range (0,11):
	if b in numbersTaken:
		continue
		print("sfsdfsfsfsf")
	else:
		print(b)

print ('- - - - - - - - - - - - - - - - - - -')

def loling():
	print("LOL")

def addOne( new_number ):
	new_number+=1
	print(new_number)

loling()
addOne(7)

print ('- - - - - - - - - - - - - - - - - - -')

def allowedDatingAge( new_age ):
	return (new_age/2)+7

williams_age = 27
print("The allowed age for you at " + str(williams_age) + " is " + str(allowedDatingAge(williams_age)))


print ('- - - - - - - - - - - - - - - - - - -')