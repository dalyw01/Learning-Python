import requests
from bs4 import BeautifulSoup
import operator

# In this directory I had to run a 
# pip install requests
# pip install bs4
# https://www.youtube.com/watch?v=up5Xehmtn2E&index=36&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_

def grabSiteText( url ):

	# Where we want to store all the words
	word_list = []

	# This is pretty much all the html text you see from "inspect element"
	source_code = requests.get(url).text

	# Grab all that source code and out into the soup object 
	soup = BeautifulSoup( source_code , features="html.parser" )

	# Only grab links with the class type identifier name
	for post_text in soup.findAll( 'h1' , {'class':'text-right'}):
		
		# Convert to string
		content = post_text.string
		
		# Make each string lower case and into respective strings and not just chars
		words = content.lower().split()

		for string in words:
			word_list.append(string)

		# Adding some dirty/bad entries
		word_list = word_list + [ ":)" , "..." , "lol!", "hello!!!!!"  ]

		# Print the list with the new bad entries
		print(word_list)

		# Print each item in the list seperatley
		for item in word_list:
			print(item)

	cleanUpList( word_list )
	createDictionary(cleanUpList( word_list ))

def cleanUpList( new_word_list ):
	print("- - - - - - - - - - - - - - -")
	print("Calling cleaning function... ")
	print("- - - - - - - - - - - - - - -")

	clean_word_list  = []
	unwanted_symbols = "!\"£$%^&*()_+<>?,./;':[]'"

	# For every word in the lists
	for word in new_word_list:
		for i in range( 0 , len( unwanted_symbols ) ):
			word = word.replace( unwanted_symbols[i] , "" )
		# If we replace e.g ":)"" with "" do not add it 
		if len(word) > 0:
			print(word)
			clean_word_list.append(word)
	return clean_word_list

def createDictionary( new_word_list ):
	print("- - - - - - - - - - - - - - -")
	print("Counting occurences...       ")
	print("- - - - - - - - - - - - - - -")

	word_count = {}

	for i in new_word_list:
		if i in word_count:
			word_count[i] +- 1
		else:
			word_count[i] = 1

	for k,v in word_count.items():
		print(k)
		print(v)


grabSiteText( "http://toscrape.com" )















