class Mario():

	def move( self ):
		print( "I am a moving!" )

class Shroom():

	def eatShroom( self ):
		print( "Now I am big!" )

class BigMario( Mario , Shroom ):
	# Python requires a class has SOMETHING
	# pass is something so it does not complain
	pass

lol = BigMario()
lol.move()
lol.eatShroom()