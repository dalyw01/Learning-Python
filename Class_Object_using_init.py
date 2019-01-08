class Tuna:

	def __init__( self ):
		# The code in here gets called straight away
		print("Hello I am a fish")

	def swim( self ):
		print( "I am swimming" )

flipper = Tuna()
# "I am a fish" gets printed despite never being called
flipper.swim()

# - - - - - - - - - - - - - - - - - - - - - - - -
# Another example
# - - - - - - - - - - - - - - - - - - - - - - - -

class Rival:

	def __init__( self , x ):
		self.energy = x

	def getEnergy( self ):
		print(self.energy)

# The enemies get energy straight away
jason = Rival(5)
ash   = Rival(22) 

jason.getEnergy()
ash.getEnergy()