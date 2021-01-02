import sys
num1 = input("Intro num 1: ")
try:
    num1 = int(num1)
except:
    print("conversion ",file=sys.stderr)
    sys.exit()