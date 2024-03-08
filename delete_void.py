#!/usr/bin/env python

def del_void():
	s = input("Enter a string: ")
	s_new = ''
	for x in s:
		if x not in s_new and x != ' ':
			s_new += x

	print(s_new)


if __name__ == "__main__":
	del_void()
