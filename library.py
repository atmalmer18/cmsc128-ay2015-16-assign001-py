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
	output = ""
	numbers = []
	size = 0
	while (num >= 0):
		if size == 9:
			# if in the millionth place
			numbers.append(10**6)
			size += 1
		if size == 4:
			# if in the thousand place
			numbers.append(10**3)
			size += 1
		if size == 2 or size == 7:
			# if number is a hundred
			tmp = numbers.pop()
			if tmp == 1:
				# will handle numbers from 10 to 19
				ones = numbers.pop()
				numbers.append(-1)
				numbers.append((tmp * 10) + ones)
			else:
				# will handle numbers from 20 to 99
				numbers.append(tmp * 10)
			numbers.append(10**2)
			size += 1
		numbers.append(num % 10)
		num = num // 10
		size += 1
		if num == 0:
			break
	for counter in range(0, size):
		# print the result one by one
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
### Logic: the word thousand and million will serve as flags whether to multiply them by 10**3 and 10**6 respectively
def wordsToNum(word):
	def switchNum (x):
		return {
			"hundred"	: 10**2,
			"thousand"	: 10**3,
			"million"	: 10**6,

			"eleven"	: 11,
			"twelve"	: 12,
			"thirteen"	: 13,
			"fourteen"	: 14,
			"fifteen"	: 15,
			"sixteen"	: 16,
			"seventeen"	: 17,
			"eighteen"	: 18,
			"nineteen"	: 19,

			"ten"		: 10,
			"twenty"	: 20,
			"thirty"	: 30,
			"forty"		: 40,
			"fifty"		: 50,
			"sixty"		: 60,
			"seventy"	: 70,
			"eighty"	: 80,
			"ninety"	: 90,
			
			"zero"		: 0,
			"one"		: 1,
			"two"		: 2,
			"three"		: 3,
			"four"		: 4,
			"five"		: 5,
			"six"		: 6,
			"seven"		: 7,
			"eight"		: 8,
			"nine"		: 9
		}.get(x, 0)
	output = []
	final = 0;
	hundreds = 0
	thousands = 0
	millions = 0
	word = word.split(" ")
	word.reverse()
	for counter in range(0, len(word)):
		# convert each to number
		tmp = word.pop()
		if tmp == "million":
			millions = hundreds * (10**6)
			hundreds = 0
		elif tmp == "thousand":
			thousands = hundreds * (10**3)
			hundreds = 0			
		else:
			hundreds += switchNum(tmp)
	final = hundreds + thousands + millions
	print(final)



### wordsToCurrency (string, string)
### Accepts two strings (number in word format, [JPY|USD|PHP]) and outputs the number with the currency
### Logic: the word thousand and million will serve as flags whether to multiply them by 10**3 and 10**6 respectively
def wordsToCurrency(word, currency):
	def switchNum (x):
		return {
			"hundred"	: 10**2,
			"thousand"	: 10**3,
			"million"	: 10**6,

			"eleven"	: 11,
			"twelve"	: 12,
			"thirteen"	: 13,
			"fourteen"	: 14,
			"fifteen"	: 15,
			"sixteen"	: 16,
			"seventeen"	: 17,
			"eighteen"	: 18,
			"nineteen"	: 19,

			"ten"		: 10,
			"twenty"	: 20,
			"thirty"	: 30,
			"forty"		: 40,
			"fifty"		: 50,
			"sixty"		: 60,
			"seventy"	: 70,
			"eighty"	: 80,
			"ninety"	: 90,
			
			"zero"		: 0,
			"one"		: 1,
			"two"		: 2,
			"three"		: 3,
			"four"		: 4,
			"five"		: 5,
			"six"		: 6,
			"seven"		: 7,
			"eight"		: 8,
			"nine"		: 9
		}.get(x, 0)
	output = []
	final = 0;
	hundreds = 0
	thousands = 0
	millions = 0
	word = word.split(" ")
	word.reverse()
	for counter in range(0, len(word)):
		# convert everything back to numbers
		tmp = word.pop()
		if tmp == "million":
			millions = hundreds * (10**6)
			hundreds = 0
		elif tmp == "thousand":
			thousands = hundreds * (10**3)
			hundreds = 0			
		else:
			hundreds += switchNum(tmp)
	final = hundreds + thousands + millions
	print(currency + ((str)(final)))



### numberDelimited (number, character, number)
### Accepts a number, a character / delimiter and another number
### First number will be used as the number itself to be printed out 
### The character will be the delimiter for the first number
### Last number will define the number of jumps for the delimiter to be placed
def numberDelimited(num, delimiter, jump):
	output = ""
	# convert string to number
	num = (str)(num)
	# separate each number 
	num = list(num)
	size = len(num) - jump
	tmp = size
	while tmp >= 0:
		# insert delimiter while length of number minus jump is not equal to 0
		num.insert(tmp,delimiter)
		tmp -= jump
	num.reverse()
	for counter in range(0, len(num)):
		# convert back as one entity
		output += (str)(num.pop())
	print(output)
	

