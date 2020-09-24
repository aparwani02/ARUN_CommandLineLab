import sys
from __init__ import *

if __name__ == '__main__':
	if len(sys.argv) - 1 == 0:
		string = noArgument()
		print(string)
	elif len(sys.argv) - 1 == 1:
		string = oneArgument(sys.argv)
		print(string)
	else:
		string = multiArgument(sys.argv)
		print(string)


