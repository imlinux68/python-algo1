#!/usr/bin/env python

def del_void():
	s = input("Enter a string: ")
	wc1 = 0
	for x in s:
		if x == ' ':
			wc1 += 1

	print(wc1 + 1)


if __name__ == "__main__":
	del_void()
