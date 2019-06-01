line = 'asdf fjdk; afed, fjek,asdf, foo' 
import re
print( re.split(r'[;,\s]\s*', line))

t1='11/22/2099'
import re
if re.match(r'\d+/\d+/\d+',t1):
    print('yoo')

import unicodedata
import sys
s = 'pýtĥöñ\fis\tawesome\r\n'

# cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) 
#     if unicodedata.combining(chr(c)))

s = '{name} has {n} messages.' 
print(s.format(name='Guido', n=37))

text = 'foo = 23 + 42 * 10'
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' 
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
print(scanner.match())

from collections import namedtuple
def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value']) 
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
# Example use
for tok in generate_tokens(master_pat, 'foo = 42'): 
    print(tok)