'''
Identifiers:
\d any number 
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
.  any character, except for a newline
\b the whitespace around words
\. a period

Modifiers:
{1,3} we're expecting 1-3
+ Match 1 or more
? Match 0 or 1 
* Match 0 or more
$ match the end of a string
^ matching the beginning of a string
| either or     \d{1=3} | \w{5-6}
[] range or "variance"			[A-Za-z]	[1-5a-qA-Z]
[x] expecting "x" ammount

White Space Characters:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

Dont Forget!
Use escape sequence in front of following if required:
. + * ? [ ] $ ^ ( ) { } | \
'''

import re

#exampleString = '''
#Jessica is 15 years old, and Daniel is 27 years old.
#Edward is 97, and his grandfather, Oscar, is 102.
#'''
#fileString = open('/etc/passwd','r')
#print(fileString)


with open("passwd.example.txt") as users:
	for line in users:
		#print(line.rstrip())
		userline= print(line.rstrip())
		print(userline)



# get all names and ages from exampleString
# define regexps to use
#ages = re.findall(r'\d{1,3}', exampleString)
nrs = re.findall(r'\d{1}', userline)
# look for all starting with capital letter and continuing small + *
users = re.findall(r'[A-Z][a-z]*', userline)

print (nrs)
print (users)


# create dictionary of values
print ("Creating dictionary ........................ done.")
valDict = {}
# we need indexing 
x = 0
for eachName in users:
	valDict[eachName] = nrs[x]
	x+=1

print (valDict)
