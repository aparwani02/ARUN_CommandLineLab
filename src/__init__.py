import sys

def noArgument(): #if there are no arguments in the command line, output the usage text
	print ("This program  accepts a varying number of command-line arguments and preforms actions based on the number of arguments provided.")
	print ("If you input zero arguments, the program will output this usage text.")
	print ("If you input one argument, the program will output whether the argument is even, odd, or not an integer.")
	print ("If you input more than one argument, the program will output the number of c's (case insensitive) in the arguments.")
	pass

def oneArgument(argv): #if there is one argument in the command line, output whether it is even, odd, or not an integer
	try:
		num = int(sys.argv[1])
		if num == 0:
			print("Zero")
		elif num % 2 == 0:
			print("Even")
		else: 
			print("Odd")
	except ValueError:
		print("Not An Integer")

def multiArgument(argv): #if there are multiple arguments in the command line, output how many c's (uppercase and lowercase) there are
	cCount = 0
	for i in (sys.argv[1:]):
		cCount += i.count('c')
		cCount += i.count('C')
	print(cCount)

if __name__ == '__main__':
    unittest.main()