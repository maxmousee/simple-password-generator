import sys
import math

def is_prime(num):
	for j in range(2,int(math.sqrt(num)+1)):
		if (num % j) == 0:
			return False
	return True

def main(argv):
	if (len(sys.argv) != 2):
		sys.exit('Usage: <char>')

	input = str(sys.argv[1])
	output = []
	for character in input:
		number = ord(character)
		output.append(number)
	low = int(output[0])
	high = low * 100
	f = open('base.txt', 'r')

	if (low == 2):
		print (2),

	if (low % 2 == 0):
		low += 1

	for x in range(0, number):
		inputtext = f.readline()

	inputtext = inputtext[:7]
	inputtext.replace(" ", "")
	lst = [word[0].upper() + word[1:] for word in inputtext.split()]
	inputtext = " ".join(lst)
	inputtext.replace(" ", "")
	for i in range(low,high,2):
		if is_prime(i):
			string = "%s %d" % (inputtext, i)
			print (string)

if __name__ == "__main__":
	main(sys.argv[1:])
