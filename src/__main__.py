import sys
from __init__ import *

if __name__ == '__main__':

	if len(sys.argv) - 1 == 0:
		noArgument()
	elif len(sys.argv) - 1 == 1:
		oneArgument(sys.argv)
	else:
		multiArgument(sys.argv)

	pass

