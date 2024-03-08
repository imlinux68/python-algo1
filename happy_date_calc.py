#!/usr/bin/env python


def date_user():
	s = input("enter your date in format dd.mm.yyyy: ")
	s1 = s.split(".")
#	print(s1)
	day = int(s1[0])
	month = int(s1[1])
	year = int(s1[2])
	sum = 0
	sum1 = 0
	while day > 0:
		sum += day % 10
		day //= 10
	while month > 0:
		sum += month % 10
		month //= 10
	while year > 0:
		sum += year % 10
		year //= 10
	while sum > 0:
		sum1 += sum % 10
		sum //= 10

	print(sum1)

if __name__ == "__main__":
	date_user()

