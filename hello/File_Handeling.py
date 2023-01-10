"""

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"""

# To read a file and print its conttnts

with open("demo.txt") as d:
	print(d.read())

# To append text to the file

with open("demo.txt","a") as d:
	d.write("Sone eddited text")
	d.close()

# To overright the file 

with open("demo.txt","w") as d:
	d.write("Over written text")
	d.close()



