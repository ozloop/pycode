import html

# **获得tuple
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    for i in attrs.items():
        print('get ',i[0],i[1])
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
    name=name,
    attrs=attr_str,
    value=html.escape(value))
    return element
# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print( make_element('item', 'Albatross', size='large', quantity=6))
# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')

from string import Template
from urllib.request import urlopen
def urlTemplate(templates):
    def op(**kwargs):
        return urlopen(templates.format_map(kwargs))
    return op
# qq=urlTemplate('http://www.qq.com?a={a}')
# for l in qq(a='aaaa'):
#     print(l)


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)
def supers(func,args,*,callback):
    result = func(*args)
    callback(result)
    return result

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

a=supers(add, (2, 3), callback=print_result)
print('result is ',a)
apply_async(add, ('hello', 'world'), callback=print_result)

