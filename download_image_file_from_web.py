import random
import urllib.request

def downloadImage(new_url):
	name = random.randrange(100)
	full_name = str(name) + " .jpg"
	urllib.request.urlretrieve( new_url , full_name )

downloadImage( "https://avatars1.githubusercontent.com/u/8547538?s=460&v=4" )