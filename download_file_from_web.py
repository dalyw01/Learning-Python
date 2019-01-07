from urllib import request

free_csv = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"

def downloadCSV( new_url ):
	response = request.urlopen( new_url )
	
	csv = response.read()
	csv_string = str(csv)
	lines = csv_string.split("\\n")

	dest_url = r"googoo.csv"

	fx = open( dest_url , "w")

	for line in lines:
		fx.write(line + "\n" )

	fx.close()

downloadCSV(free_csv)