while True:
	try:
		number = int(input("You've entered the loop, enter a number lol\n"))
		print( number * 18  )
		break
	except ValueError:
		print("ERROR! Make sure you enter a number")
	except ZeroDivisionError:
		print("Don't pick zero!!!!")
	except:
		# Except is general error, nice but hides source problem
		break # Screw it, I'm breaking out
	finally:
		# Finally occurs no matter what
		print("Exiting loop!")