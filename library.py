# Author: Almer T. Mendoza
# CMSC 128 AB - 6L

## A LIBRARY THAT IMPLEMENTS THE FOLLOWING
## 1. Converting number to words 
## 2. Converting words to numbers
## 3. Converting words to currency
## 4. Inserting delimiter to a number

import sys

### numToWords (number)
### Accepts a whole number and outputs an equivalent in word form
def numToWords(num):
	output = ""
	numbers = []
	size = 0
	while (num >= 0):
		if size == 9:
			numbers.append(10**6)
			size += 1
		if size == 4:
			numbers.append(10**3)
			size += 1
		if size == 2 or size == 7:
			tmp = numbers.pop()
			if tmp == 1:
				ones = numbers.pop()
				numbers.append(-1)
				numbers.append((tmp * 10) + ones)
			else:
				numbers.append(tmp * 10)
			numbers.append(10**2)
			size += 1
		numbers.append(num % 10)
		num = num // 10
		size += 1
		if num == 0:
			break
	for counter in range(0, size):
		def getTens (y):
			return {
				10: "ten",
				11: "eleven",
				12: "twelve",
				13: "thirteen",
				14: "fourteen",
				15: "fifteen",
				16: "sixteen",
				17: "seventeen",
				18: "eighteen",
				19: "nineteen",
			}.get(y)
		def switchNum (x):
			return {
				10**6: "million",
				10**3: "thousand",
				10**2: "hundred",
				20: "twenty",
				30: "thirty",
				40: "fourty",
				50: "fifty",
				60: "sixty",
				70: "seventy",
				80: "eighty",
				90: "ninety",
				0: "zero",
				1: "one",
				2: "two",
				3: "three",
				4: "four",
				5: "five",
				6: "six",
				7: "seven",
				8: "eight",
				9: "nine",
			}.get(x, x)
		digit = numbers.pop()
		if digit >= 10 and digit <= 19:
			sys.stdout.write(switchNum(getTens(digit)) + " ")
		elif digit == -1:
			sys.stdout.write("")
		else:
			sys.stdout.write(switchNum(digit) + " ")
	print("")

### wordsToNum (string)
### Accepts a number in word form and returns its equivalent in number format
def wordsToNum(word):
	output = 0
	print(output)



### wordsToCurrency (string, string)
### Accepts two strings (number in word format, [JPY|USD|PHP]) and outputs the number with the currency
def wordsToCurrency(word, currency):
	output = 0
	print(output)



### numberDelimited (number, character, number)
### Accepts a number, a character / delimiter and another number
### First number will be used as the number itself to be printed out 
### The character will be the delimiter for the first number
### Last number will define the number of jumps for the delimiter to be placed
def numberDelimited(num, delimiter, jump):
	output = 0
	print(output)
	
	
	