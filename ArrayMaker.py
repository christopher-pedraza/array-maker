# Default values
WRAPPER = "'"
NAME = "board"
DATATYPE = "char[,] "
INPUTFILE = "input.txt"

def createArray(wrapper=WRAPPER, name=NAME, dataType=DATATYPE, inputFile=INPUTFILE):
	# Add the name and datatype of the array
	res = f"{dataType}{name} = ["

	# Open the text file
	with open(inputFile) as f:
		# Iterate over the lines
		for line in f.readlines():
			res += "["
			# If the last character is a NEWLINE, remove it
			if line[-1] == "\n":
				line = line[:-1]
			# Iterate over the chars in each line split by a tab
			for char in line.split("\t"):
				# If the char isn't empty, add it to the string
				if char != "":
					res += f"{wrapper}{char}{wrapper},"
			# Remove the last comma and close the inner list
			res = f"{res[:-1]}], "

	# Remove the last space and comma and close the outer list
	res = f"{res[:-2]}]"

	return res

print(createArray())