#! /usr/bin/env python

import collections
def main():
	q = collections.deque()
	print(q)
	q.append(2)
	q.append(3)
	q.append(10)
	print(q)


if __name__ == "__main__":
	main()
