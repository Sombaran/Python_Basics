BASIC
In [6]:
1+2
Out[6]:
3
In [7]:
1*3
Out[7]:
3
In [15]:
1.0/2
Out[15]:
0.5
In [24]:
45.0//2
Out[24]:
22.0
In [25]:
45.0//2.0
Out[25]:
22.0
In [26]:
45.0//2.0
Out[26]:
22.0
In [10]:
2**2
Out[10]:
4
In [27]:
1.000000
Out[27]:
1.0
In [28]:
2 + 3 * 5 + 5
Out[28]:
22
In [29]:
(2+3) * (5+5)
Out[29]:
50
In [30]:
4 % 2
Out[30]:
0
In [31]:
2%4
Out[31]:
2
In [1]:
3%4
Out[1]:
3
In [3]:
var=2
In [4]:
var
Out[4]:
2
In [13]:
type(var)
Out[13]:
int
In [14]:
id(var)
Out[14]:
140249612208896
In [15]:
type(var)
Out[15]:
int
In [16]:
var=var+var
In [17]:
var
Out[17]:
16
In [42]:
id(var)
Out[42]:
140293618387584
In [43]:
var is var
Out[43]:
True
In [44]:
var=var+var
In [45]:
var
Out[45]:
8
In [46]:
id(var)
Out[46]:
140293618387712
SRINGS
In [47]:
'First way of creating a string'
Out[47]:
'First way of creating a string'
In [48]:
"Second way of creating a string"
Out[48]:
'Second way of creating a string'
In [20]:
"I can\'t\' go"
Out[20]:
"I can't' go"
In [66]:
x="hello"
In [67]:
x
Out[67]:
'hello'
In [68]:
print(x)
hello
In [70]:
roll_no=23
name="SOM"
In [75]:
'My name is {0} and my roll_no is {1}'.format(name,roll_no)
Out[75]:
'My name is SOM and my roll_no is 23'
In [76]:
print('My name is {0} and my roll_no is {1}'.format(name,roll_no))
My name is SOM and my roll_no is 23
In [79]:
print('My name is {one_1} and my roll_no is {two_2},more {one_1}'.format(one_1=name,two_2=roll_no))
My name is SOM and my roll_no is 23,more SOM
In [80]:
s='abcdefghijkl' 
In [81]:
s
Out[81]:
'abcdefghijkl'
In [82]:
id(s)
Out[82]:
140293431596592
In [84]:
type(s)
Out[84]:
str
In [85]:
s[0]
Out[85]:
'a'
In [86]:
len(s)
Out[86]:
12
In [88]:
s[11]
Out[88]:
'l'
In [89]:
s[::]
Out[89]:
'abcdefghijkl'
In [90]:
s[::-1]
Out[90]:
'lkjihgfedcba'
In [92]:
s[::-3]
Out[92]:
'lifc'
In [93]:
s[:3]
Out[93]:
'abc'
In [94]:
s
Out[94]:
'abcdefghijkl'
In [95]:
s[3:6]
Out[95]:
'def'
In [33]:
s1='foo' 
s2='foo'
s3='boo'
In [34]:
id(s1)
Out[34]:
140249549508144
In [35]:
id(s2)
Out[35]:
140249549508144
In [36]:
id(s3)
Out[36]:
140249537181040
In [38]:
s1 is s2 is s3
Out[38]:
False
In [39]:
s1 is s3
Out[39]:
False
In [40]:
s2 is s3
Out[40]:
False
In [41]:
del (s1,s2)
In [111]:
course="PGDIoT"
count=0
for letter in course:
    count=count+1
print("Total length of string is",count)
Total length of string is 6
In [115]:
word = 'banana'
index = word.find('a')
print (index)
1
In [43]:
word = 'banana'
index = word.rfind('a')
print (index)
print(word.find('na', 1,6))
print(word.find('na', 4))
5
2
4
In [44]:
print(type(word))
<class 'str'>
In [128]:
# take input from the user
my_str = input("Enter a string: ")
# reverse the string
rev_str = ''.join(reversed(my_str))
# check if the string is equal to its reverse
if my_str == rev_str:
    print("It is palindrome")
else:
    print("It is not palindrome")
Enter a string: mom
It is palindrome
LISTS
In [129]:
[1,2,3]
Out[129]:
[1, 2, 3]
In [130]:
['a','b','c',1,2,4]
Out[130]:
['a', 'b', 'c', 1, 2, 4]
In [47]:
my_lst=['a',1,'b',2]
In [48]:
print(my_lst)
['a', 1, 'b', 2]
In [49]:
print(id(my_lst))
140249408495240
In [50]:
print(type(my_lst))
<class 'list'>
In [51]:
my_lst.append('c')
In [52]:
my_lst
Out[52]:
['a', 1, 'b', 2, 'c']
In [53]:
my_lst.append(3)
#if you need to add more than one argument then use extend function
In [54]:
print(my_lst)
['a', 1, 'b', 2, 'c', 3]
In [55]:
my_lst[0]
Out[55]:
'a'
In [56]:
my_lst[1]='A'
In [57]:
my_lst[3]='B'
In [58]:
my_lst[5]='C'
In [59]:
print(my_lst)
['a', 'A', 'b', 'B', 'c', 'C']
In [145]:
my_lst[::-1]
Out[145]:
['C', 'c', 'B', 'b', 'A', 'a']
In [68]:
print(my_lst)
['a', 'A', 'b', 'B', 'c', 'C', '1', '1', '4', '4', '1']
In [69]:
my_lst.extend('1')
In [70]:
print(my_lst)
['a', 'A', 'b', 'B', 'c', 'C', '1', '1', '4', '4', '1', '1']
In [71]:
 movies = [ "Ice Age", "Gravity", "Rio"]
In [72]:
movies.append("The")
print(movies)
['Ice Age', 'Gravity', 'Rio', 'The']
In [73]:
movies.extend("Rio")
print(movies)
['Ice Age', 'Gravity', 'Rio', 'The', 'R', 'i', 'o']
In [74]:
nest_lst=[1,2,[3,4]]
In [175]:
print(nest_lst)
[1, 2, [3, 4]]
In [176]:
nest_lst[2]
Out[176]:
[3, 4]
In [177]:
nest_lst[2][0]
Out[177]:
3
In [178]:
nest_lst[2][1]
Out[178]:
4
In [88]:
print(id(nest_lst))
140249408643528
In [104]:
print(type(nest_lst))
<class 'list'>
In [98]:
rest_lst=[1,2,3,[4,5,['JingJong']]]
In [99]:
print(rest_lst)
[1, 2, 3, [4, 5, ['JingJong']]]
In [100]:
print(id(rest_lst))
140249408663240
In [105]:
print(type(rest_lst))
<class 'list'>
In [106]:
#nest_lstreplica=[1,2,3,[4,5,['JingJong']]]
nest_lstreplica=rest_lst
In [107]:
print(nest_lstreplica)
[1, 2, 3, [4, 5, ['JingJong']]]
In [108]:
print(id(nest_lstreplica))
140249408663240
In [110]:
rest_lst is nest_lstreplica
Out[110]:
True
In [135]:
a=[1,2,3]
b=[1,2,3]
In [146]:
a is b
Out[146]:
True
In [147]:
print(id(a))
print(id(b))
140249408223368
140249408223368
In [148]:
print(type(a))
print(type(b))
<class 'list'>
<class 'list'>
In [149]:
s1='foo' 
s2='foo'
In [150]:
s1 = s2
In [139]:
print(id(s1))
print(id(s2))
140249549508144
140249549508144
In [140]:
print(type(s1))
print(type(s2))
<class 'str'>
<class 'str'>
In [151]:
s1=['foo'] 
s2=['foo']
In [158]:
s1 is s2
Out[158]:
True
In [159]:
print(id(s1))
print(id(s2))
140249408223496
140249408223496
In [1]:
print(movies)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-d4351313a7b4> in <module>()
----> 1 print(movies)

NameError: name 'movies' is not defined
In [235]:
len(movies)
Out[235]:
7
In [247]:
movies.insert(3,'blue')
In [248]:
print(movies)
['Ice Age', 'ice age2', 'ice age3', 'blue', 'ice age2', 'ice age2', 'ice age3', 'ice age2', 'ice age3', 'ice age3', 'Gravity', 'Rio', 'blue', 'The', 'R', 'i', 'o']
In [249]:
movies[1:1]=("ice age2","ice age3")
In [246]:
print(movies)
['Ice Age', 'ice age2', 'ice age3', 'ice age2', 'ice age2', 'ice age3', 'ice age2', 'ice age3', 'ice age3', 'Gravity', 'Rio', 'blue', 'The', 'R', 'i', 'o']
In [252]:
movies.reverse()
In [253]:
print(movies)
['Ice Age', 'ice age2', 'ice age3', 'ice age2', 'ice age3', 'blue', 'ice age2', 'ice age2', 'ice age3', 'ice age2', 'ice age3', 'ice age3', 'Gravity', 'Rio', 'blue', 'The', 'R', 'i', 'o']
In [254]:
movies.pop()
Out[254]:
'o'
In [255]:
movies.pop()
Out[255]:
'i'
In [256]:
movies.sort()
In [263]:
print(movies)
['Gravity', 'Ice Age', 'R', 'Rio', 'The', 'blue', 'blue', 'ice age2', 'ice age2', 'ice age2', 'ice age2', 'ice age2', 'ice age3', 'ice age3', 'ice age3', 'ice age3', 'ice age3']
In [266]:
print(movies.clear())
None
In [269]:
del(movies)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-269-5f93885e2822> in <module>()
----> 1 del(movies)

NameError: name 'movies' is not defined
In [270]:
a
Out[270]:
[1, 2, 3]
In [271]:
b=a[:]
In [272]:
print(a,b)
[1, 2, 3] [1, 2, 3]
In [273]:
id(a)
Out[273]:
140293431302920
In [274]:
id(b)
Out[274]:
140293431308552
CLOANING OF LIST
In [275]:
a
Out[275]:
[1, 2, 3]
In [276]:
b
Out[276]:
[1, 2, 3]
In [277]:
a is b
Out[277]:
False
ALIASING
In [286]:
A=[1,2,3]
In [287]:
B=A
In [288]:
B
Out[288]:
[1, 2, 3]
In [289]:
A
Out[289]:
[1, 2, 3]
In [298]:
B is A
Out[298]:
True
In [299]:
A is B
Out[299]:
True
In [292]:
id(A)
Out[292]:
140293431716360
In [293]:
id(B)
Out[293]:
140293431716360
In [294]:
A is A
Out[294]:
True
In [295]:
A is B
Out[295]:
True
In [296]:
B is B
Out[296]:
True
In [301]:
my_fam=["Rekha","Uday","Oien"]
for Som in my_fam: print(Som)
Rekha
Uday
Oien
In [304]:
my_fam=["Rekha","Uday","Oien"]
for (SNo, Value) in enumerate (my_fam): print(SNo,Value)
0 Rekha
1 Uday
2 Oien
In [7]:
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
In [11]:
[[row[i] for row in matrix] for i in range(4)] 
Out[11]:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
In [331]:
list()
x = (x **2 for x in range(20))
In [333]:
print(list(x))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
In [334]:
tuple()
x = (x **2 for x in range(20))
print(tuple(x))
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361)
In [335]:
str()
x = (x **2 for x in range(20))
print(str(x))
<generator object <genexpr> at 0x7f989c24b410>
In [340]:
a
Out[340]:
[1, 2, 3]
In [341]:
b
Out[341]:
[1, 2, 3]
In [349]:
zipped = zip(a,b)
In [350]:
print(zipped)
<zip object at 0x7f989c248588>
In [348]:
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
transpose = list(zip(*matrix))
print(transpose)
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
In [351]:
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
matrix = [[row[i] for row in matrix] for i in range(4)]
print(matrix)
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
DICTONARIES
In [362]:
d1={'k1':'v1',
    'k2':'v2'}
In [363]:
d1
Out[363]:
{'k1': 'v1', 'k2': 'v2'}
In [364]:
d2=dict({'k1':'v1','k2':'v2'})
In [365]:
d2
Out[365]:
{'k1': 'v1', 'k2': 'v2'}
In [366]:
d1 == d2
Out[366]:
True
In [367]:
id(d1)
Out[367]:
140293431381064
In [368]:
id(d2)
Out[368]:
140293431667656
In [369]:
del(d2)
In [372]:
d1['k1']
Out[372]:
'v1'
In [373]:
d1['k2']
Out[373]:
'v2'
In [374]:
d2={
   'k1':[1,2,3],
    'k2':["ram","rahim"]
}
In [375]:
d2['k1']
Out[375]:
[1, 2, 3]
In [376]:
d2['k1'][0]
Out[376]:
1
In [377]:
d2['k1'][1]
Out[377]:
2
In [379]:
d2['k1'][2]
Out[379]:
3
In [381]:
dict_lst =d2['k1']
In [382]:
print(dict_lst)
[1, 2, 3]
NESTED DICTONARIES
In [383]:
d= {
    'k2':{'innerkey':[1,2,3]}
}
In [384]:
d
Out[384]:
{'k2': {'innerkey': [1, 2, 3]}}
In [390]:
d_lst=d['k2']['innerkey']
In [391]:
print(d_lst)
[1, 2, 3]
In [397]:
d1
Out[397]:
{'k1': 'v1', 'k2': 'v2'}
In [398]:
for i in d1: print(i)
k2
k1
In [400]:
for i in d1: print(d1[i])
v2
v1
In [401]:
len(d1)
Out[401]:
2
In [402]:
di=iter(d1)
In [403]:
next(di)
Out[403]:
'k2'
In [404]:
next(di)
Out[404]:
'k1'
In [407]:
str(d1)
Out[407]:
"{'k2': 'v2', 'k1': 'v1'}"
In [409]:
d1.setdefault('k3','v3')
Out[409]:
'v3'
In [415]:
d1
Out[415]:
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
In [417]:
for i in d1:
    print(i)
    print(d1[i])
k2
v2
k3
v3
k1
v1
In [418]:
d1.setdefault('k4')
In [420]:
d1
Out[420]:
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': None}
In [421]:
for i in d1:
    print(i)
    print(d1[i])
k4
None
k2
v2
k3
v3
k1
v1
In [429]:
d1.update(k4='v4')
In [430]:
d1
Out[430]:
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
In [432]:
for i in d1:
    print(i)
    print(d1[i])
k4
v4
k2
v2
k3
v3
k1
v1
BOOLEAN
In [434]:
True
Out[434]:
True
In [435]:
False
Out[435]:
False
In [436]:
None
SET
In [438]:
#set is a collection of unique elements
{1,2,3}
Out[438]:
{1, 2, 3}
In [440]:
{1,1,1,1,2,2,2,3,3}
Out[440]:
{1, 2, 3}
In [441]:
set([1,1,1,1,2,2,2,3,3,3])
Out[441]:
{1, 2, 3}
In [442]:
s={1,5,5,7}
In [443]:
s
Out[443]:
{1, 5, 7}
In [446]:
s.add(8)
In [447]:
s
Out[447]:
{1, 5, 7, 8}
In [448]:
s.add(5)
In [449]:
s
Out[449]:
{1, 5, 7, 8}
COMPARISON OPERATOR
In [450]:
1>2
Out[450]:
False
In [451]:
1<2
Out[451]:
True
In [452]:
1>=2
Out[452]:
False
In [453]:
1<=1
Out[453]:
True
In [454]:
1 == 1
Out[454]:
True
In [455]:
1 == 2
Out[455]:
False
In [456]:
1 != 1
Out[456]:
False
In [457]:
'hi' == 'bye'
Out[457]:
False
In [458]:
1<2 and 2<4
Out[458]:
True
In [459]:
1>2 and 2<4
Out[459]:
False
In [460]:
1>2 or 2<4
Out[460]:
True
In [462]:
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('last')
middle
FOR and WHILE LOOPS
In [13]:
seq=[1,2,3,4]
In [14]:
for item in seq:
    #for item in range(4):
    print(item)
    #print(range(4))
1
2
3
4
In [18]:
for item in seq:
    for item in range(4):
        print(item)
        print(range(4))
0
range(0, 4)
1
range(0, 4)
2
range(0, 4)
3
range(0, 4)
0
range(0, 4)
1
range(0, 4)
2
range(0, 4)
3
range(0, 4)
0
range(0, 4)
1
range(0, 4)
2
range(0, 4)
3
range(0, 4)
0
range(0, 4)
1
range(0, 4)
2
range(0, 4)
3
range(0, 4)
In [19]:
i=1
while i < 5:
    print('The value of i is {0}'.format(i))
    i=i+1
The value of i is 1
The value of i is 2
The value of i is 3
The value of i is 4
In [15]:
#create list of range
list(range(9))
Out[15]:
[0, 1, 2, 3, 4, 5, 6, 7, 8]
In [8]:
list
Out[8]:
list
In [16]:
seq
Out[16]:
[1, 2, 3, 4]
In [25]:
li = []
for i in seq: 
    li.append(i ** 2) 
    print(li)
print(li)
[1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]
[1, 4, 9, 16]
LIST COMPREHENSION
In [31]:
li = [i ** 2 for i in seq if i%2 == 0]
In [32]:
print(li)
[4, 16]
FUNCTIONS
In [43]:
def my_fnc(passhere):
    print(passhere)
my_fnc('hailo')
hailo
In [44]:
def my_fnc(passhere = 'Default Name'):
    print('hello ' + passhere)
my_fnc('Oien')
hello Oien
In [20]:
def my_fnc(passhere ):
    print('hello ' + passhere)
my_fnc('Oien')
hello Oien
In [45]:
my_fnc
Out[45]:
<function __main__.my_fnc>
In [50]:
def my_sqr(num):
    '''
    THIS IS 
    A DOC STRING
    '''
    return (num ** 2)
result = my_sqr(4)
print(result)
16
In [52]:
my_sqr
Out[52]:
<function __main__.my_sqr>
