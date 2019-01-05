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