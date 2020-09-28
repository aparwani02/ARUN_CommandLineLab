import sys
from __init__ import *

def main(args):
	if len(sys.argv) == 1:
		string = noArgument()
		print(string)
	elif len(sys.argv) == 2:
		string = oneArgument(args[1])
		print(string)
	else:
		string = multiArgument(args)
		print(string)

if __name__ == '__main__':
	main(sys.argv)
