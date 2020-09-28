def noArgument(): #if there are no arguments in the command line, output the usage text
	return ("This program accepts a varying number of command-line arguments and preforms actions based on the number of arguments provided. If you input zero arguments, the program will output this usage text. If you input one argument, the program will output whether the argument is even, odd, or not an integer. If you input more than one argument, the program will output the number of c's (case insensitive) in the arguments.")

def oneArgument(parameter): #if there is one argument in the command line, output whether it is even, odd, or not an integer
	if parameter.isdigit() and (parameter.count(".") == 0):
		if int(parameter) == 0:
			return 'Zero'
		elif int(parameter) % 2 == 0:
			return 'Even'
		else:
			return 'Odd'
	else:
		return 'Not An Integer'

def multiArgument(parameterArray): #if there are multiple arguments in the command line, output how many c's (uppercase and lowercase) there are
	cCount = 0
	for i in range(1, len(parameterArray)):
		cCount += parameterArray[i].lower().count("c")
	return cCount