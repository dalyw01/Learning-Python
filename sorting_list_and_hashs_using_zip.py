stocks = {
	'GOOGLE' : 500,
	'FB' : 10,
	'YAHOO' : 5,
	'Z' : 6,
	'AMZ' : 350,
	'APPLE' : 450,
}

# I want the values displayed first
# zip( stocks.values(), stocks.keys() )

print("- - - - - - - - - - - - - - - - - - - - -")

print(max(zip( stocks.values(), stocks.keys())))
print(max(zip( stocks.keys(), stocks.values())))

print("- - - - - - - - - - - - - - - - - - - - -")

print(min(zip( stocks.values(), stocks.keys())))
print(min(zip( stocks.keys(), stocks.values())))

print("- - - - - - - - - - - - - - - - - - - - -")

print(stocks.values(), stocks.keys())
print(sorted(zip( stocks.values(), stocks.keys())))

print("- - - - - - - - - - - - - - - - - - - - -")

first_list   = [ 'Bucky'   , 'Tom'   , 'Time' ]
surname_list = [ 'Roberts' , 'Hanks' , 'Swift'] 

names = zip( first_list , surname_list )

for a,b in names:
	print(a,b)
