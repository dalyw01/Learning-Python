class Girl:

	# Anytime an object is made using this class, will have this variable
	gender = "female"

	# Every girl will be female, but every girl will have a different name
	def __init__( self , name ):
		self.name = name

girl_1 = Girl("Rachel")
girl_2 = Girl("Aimee")

print(girl_1.gender)
print(girl_2.gender)

# If I do this below Python complains that I NEED to include a "name"
# girl_3 = Girl()
# print(girl_3.gender)

# - - - - - - - - - - - - - - - - - - - - - - - -
# Another example
# - - - - - - - - - - - - - - - - - - - - - - - -

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make  = make
        self.model = model

mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
# 4
print (Car.wheels)
# 4