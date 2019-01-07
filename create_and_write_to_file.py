# Creating and writing to file
wills_file = open( "sample.txt" , "w" )
wills_file.write("Writing some stuff in here like, I'm from Cork baiiiii\n")
wills_file.write("Cork baiiiii\n")
wills_file.write("DERP DERP DERP\n")
wills_file.close()

# Printing the file to the log
fr = open( "sample.txt" , "r" )
text = fr.read()
print(text)
fr.close()