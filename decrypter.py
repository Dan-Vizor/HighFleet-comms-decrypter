#!/usr/bin/python3

"""
MIT License

Copyright (c) 2021 Dan Vizor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

https://pypi.org/project/cipher-solver/
"""

import os

# Caesar cipher
def DecryptCaesar(CypherText:str, key:int):
	out = ""
	for char in CypherText.lower():
		if ord(char) not in range(ord('a'), ord('z')+1):
			out += char
			continue

		ClearOrd = ord(char) - key
		if ClearOrd < ord('a'): ClearOrd += 26

		out += chr(ClearOrd)

	return out

def DecryptSubstitution(CypherText:str, key:dict):
	out = ""

	return out

# import the common words list from file
CommonWords = [i.rstrip() for i in open("1-100k.txt", "r")]

# get input from user
CypherText = input("enter cyphertext: ")

# try every avalable key for a likely decrypt
results = []
for key in range(1, 26):
	ClearText = DecryptCaesar(CypherText, key)

	# count the number of words that appear in the common words list
	FoundWords = 0
	for word in ClearText.split(" "):
		for CommonWord in CommonWords:
			if word == CommonWord: FoundWords += 1

	results.append({"ClearText": ClearText, "key": key, "FoundWords": FoundWords})

# sort results by number of found results
results = sorted(results, key=lambda k: k['FoundWords'], reverse=True)

# get command line width for output styling
CMDWidth = os.get_terminal_size().columns

#print results to user
if [result['FoundWords'] for result in results][0] > 5:
	for result in results:
		if result['FoundWords'] > 5:
			OutMessage = f"{result['ClearText']}"
			OutKey = f"== key {result['key']} "

			if len(OutMessage) <= CMDWidth:
				print(f"\n{OutKey}{'='*(len(OutMessage)-len(OutKey))}\n{OutMessage}\n{'='*len(OutMessage)}")

			else:
				print(f"\n{'='*CMDWidth}\n{OutMessage}\n{'='*CMDWidth}")

# if no clear decrypts are found (or a very short message was entered) 
else:
	if len(CypherText.split(" ")) < 5: print("No likely decrypts found, showing low quality results.")

	for result in sorted(results, key=lambda k: k['key']):
		OutMessage = f"{result['ClearText']}"
		OutKey = f"== key {result['key']} "

		if len(OutMessage) <= CMDWidth:
			print(f"\n{OutKey}{'='*(len(OutMessage)-len(OutKey))}\n{OutMessage}\n{'='*len(OutMessage)}")

		else:
			print(f"\n{'='*CMDWidth}\n{OutMessage}\n{'='*CMDWidth}")