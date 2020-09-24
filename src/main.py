import sys
print ("step one")
if len(sys.argv) - 1 == 0:
    print("you did it")
elif len(sys.argv) - 1 == 1:
    print("one argument")
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
elif len(sys.argv) - 1 > 1:
    cCount = 0
    for i in (sys.argv):
        print(i)
        if "c" in str(i) or "C" in str(i):
            cCount +=1
    print(cCount)