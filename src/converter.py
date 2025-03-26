import os
import sys


def shortest(s1, s2):
	'''Return the shortest string'''

	if len(s1) < len(s2):
		return s1
	return s2


def convert(src):
	'''Convert a string into Brainfuck code'''

	res = ""
	arr = [0]
	idx = 0
	for c in src:
		while arr[idx] != ord(c):
			if arr[idx] - ord(c) < 0:
				arr[idx] += 1
				res += '+'
			else:
				arr[idx] -= 1
				res += '-'
		res+='.'

	return res


def main():
	'''The main function of the script'''

	src = ""
	dest = sys.stdout
	if len(sys.argv) > 1 and os.path.exists(sys.argv[1].strip()):
		src = open(sys.argv[1]).read()
	else:
		src = input("$> ")

	if len(sys.argv) > 2:
		dest = open(sys.argv[2], "w+")

	# src = "A"

	res = convert(src)

	print(res, file=dest)


if __name__ == "__main__":
	main()

