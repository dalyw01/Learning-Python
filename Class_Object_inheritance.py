class Parent():

	def printLastName( self ):
		print( "Daly" )

class Child( Parent ):
	
	def printFirstName( slef ):
		print( "William" )

	# Can be overwritten
	def printLastName( self ):
		print( "Bryer" ) 


third_child = Child()
third_child.printLastName()
third_child.printFirstName()