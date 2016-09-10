RegExp
Created Friday 09 May 2014

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
[] range or "variance"          [A-Za-z]    [1-5a-qA-Z]
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

