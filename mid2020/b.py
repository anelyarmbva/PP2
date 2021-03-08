import re

txt = input()
word = input()
a = re.search(word, txt)
position = a.span()
if a:
    print('First time',  word,  'occured in position:', position[0], sep = ' ')
else:
    print('Not found')