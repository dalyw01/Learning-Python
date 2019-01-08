class Enemy:

	life = 3

	# Self is like This in Java, it refers to the current object
	def attack( self ):
		print( "ouch!" )
		self.life -= 1
		hp -= 1

	def checkLife( self ):
		if self.life <= 0:
			print( "I am dead" )
		else:
			print( "[ " + str(self.life) + " ] life left" )

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.checkLife()
enemy2.checkLife()

enemy1.attack()
enemy1.attack()
enemy1.attack()

enemy1.checkLife(
)enemy1.checkHp()
enemy2.checkLife()