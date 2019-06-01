

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    def print(self):
        for i in self._queue:
            print('..',i)

q=PriorityQueue()
q.push(1,1)
q.push(5,5)
q.push(4,4)
q.push(11,1)
q.print()
print(q.pop(),q.pop(),q.pop(),q.pop())


from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print('list ',d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print('set',d)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print( min(zip(prices.values(),prices.keys())))

def dedupe(items): 
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10] 
print(list(dedupe(a)))

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
print(word_counts)

from operator import itemgetter
ss=[{'a':1,'b':2},{'a':11,'b':22},{'a':3,'b':42},{'a':51,'b':21}]
print(sorted(ss,key=itemgetter('a')))

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter 
from itertools import groupby
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date) 
    for i in items:
        print(' ', i)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
p1=dict((k,v) for k,v in prices.items() if v > 50)
print(p1)