# _*_ coding: utf-8 _*_
import random
from math import pi,sqrt
# Base Concepts 基础概念
print('---------------------------------Base Concepts-----------------------------')
print('Hello World!')
#-- quit() 退出控制台

print("\n")
# Control Structures 控制流
print('-------------------------------Control Structures---------------------------')
#--   List 集合
words = ["Hello","world",'!']
print(words[0])
print(words[1])
print(words[2])
empty_list = []
print(empty_list)
number = 3
things =["string",0,[1,2,number],4.56]
print(things[1])
print(things[2])
print(things[2][2])
#   List Operations 集合运算
nums = [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
#--   List Functions 集合函数
nums.append(4)
print(nums)
print(len(nums))
words = ['Python','fun']
index = 1
words.insert(index,'is')
print(words)
letters = ['p','q','r','s','p','u']
print(letters.index('r'))
print(letters.index('p'))
    #print(letters.index('k')) ValueError: 'k' is not in list
#--   Range 范围
numbers = list(range(10))
print(numbers)
numbers = list(range(3,8))
print(numbers)
print(range(20) == range(0,20))
numbers = list(range(5,20,2))
print(numbers)
#--   For Loop
counter = 0
max_index = len(words) -1
while(counter <= max_index):
    word = words[counter]
    print(word + '!')
    counter = counter + 1
for word in words :
    print(word + '!')
for i in range(5):
    print('Hello!')
for i in range(0,20,2):
    print(i)
#-- Creating a Calculator
#while true:
#    print("Options:")
#    print("Enter 'add' to add two numbers")
#    print("Enter 'substract' to subtract two numbers")
#    print("Enter 'multiply' to multiply two numbers")
#    print("Enter 'divide' to divide two numbers")
#    print("Enter 'quit' to end the program")
#    user_input = input(":")
#    if user_input == 'quit':
#        break
#    elif user_input == "add":
#        break
#    elif user_input == "substract":
#        break
#    elif user_input == "multiply":
#        break
#    elif user_input == "divide":
#    else:
#        print("Unknown input")
#        break
# Function & Modules 函数和模块
print('-------------------------------Function & Modules---------------------------')
#-- Code Reuse
# Don't Repeat Yourself
#-- Functions函数
range(2,20)
print(range(2,20))
print(str(12))
print(range(10,20,3))
def my_func():
    print("Joey")
    print("Joey")
    print("Joey")

my_func()

def print_with_exclamation(word):
    print(word+'!')
print_with_exclamation("Joey")

def function(variable):
    variable += 1
    print(variable)
function(7)
#print(variable)
def max(x,y):
    if x>=y:
        return x
    else:
        return y
print(max(4,7))
z = max(8,5)
print(z)
def add_numbers(x,y):
    total = x + y
    return total
    print("This won't be printed")
print(add_numbers(4,5))
#-- Comments & Docstrings
def shout(word):
    """
    print a word with an exclamationg mark following it.
    """
    print(word+"!")
shout("Hello Joey")
#-- Functions as Objects 把函数当作参数传递给函数
def multiply(x,y):
    return x * y
a = 4
b = 7
operation = multiply
print(operation(a,b))

def add(x,y):
    return x + y
def do_twice(func,x,y):
    return func(func(x,y),func(x,y))
a = 5
b = 10
print(do_twice(add,a,b))
#-- Modules 模块
for i in range(5):
    value = random.randint(1,6)
    print(value)
print(pi)
print(sqrt(100))
# Exceptions & Files
print('-------------------------------Exceptions & Files---------------------------')
#-- Exception Handling 异常处理
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
except ValueError:
    print("Value error ocurred")
#-- Finally
finally:
    print("This code will run no matter what")
#-- Raising Exceptions
name = "1234"
#rase NameError("Invlid name!")
#-- Assertions 断言？
print(1)
assert 2 + 2 == 4
print(2)
#assert (1 + 1 = 3) ,"Wrong!"
print(3)
#-- Opening Files  打开文件
myfile = open("filename.txt")
cont = myfile.read()
print(cont)
myfile.close()
file = open("filename.txt","r")
print(file.readlines())
file.close()
file = open("filename.txt","r")
for line in file:
    print(line)
file.close()
file = open("filename.txt","w")
file.write("This has been written to a file!")
file.close()
file = open("filename.txt","r")
print(file.read())
file.close()
#Working with Files
with open("filename.txt") as f:
    print(f.read())
print('-------------------------------More Types---------------------------')
#-- None
None == None
print(None)
def some_fun():
    print("Hi")
var = some_fun()
print(var)
#-- Dictionaries
ages = {"Dave":24,"Mary":42,"John":58}
print(ages["Dave"])
print(ages["Mary"])
primary = {
    "red":[255,0,0],
    "green":[0,255,0],
    "blue":[0,0,255]
}
print(primary["red"])
squares = {1:1,2:4,3:"error",4:16}
squares[8] = 64
squares[2] = 9
print(squares)
nums ={
    1:"one",
    2:"two",
    3:"three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
pairs = {1:"apple",
    "orange":[2,3,4],
    True:False,
    None:"True",}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345,"not in dictionary"))
#-- Tuples 元组
words = ("spam","eggs","sausages")
print(words[0])
#words[1] = "cheese" 不可变的，所以不能赋值
my_typule = "one","two","three"
print(my_typule[0])
#-- List Slices
squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print(squares[:6])
print(squares[2:])
print(squares[::2])  #有点难记住，标记下
print(squares[2:8:3])
print(squares[1:-2])
print(squares[7:5:-1]) #没理解
#-- List Comprehensions
cubes = [i**3 for i in range(5)]
print(cubes)
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
#-- String Formatting
nums = [4,5,6]
msg = "Numbers:{0}{1}{2}".format(nums[0],nums[1],nums[2])
print(msg)
a = "{x},{y}".format(x=5,y=12)
print(a)
#-- Useful Functions
print(",".join(["spam","eggs","ham"]))
print("Hello ME".replace("ME","world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".upper())
print("This is a sentence.".lower())
print("spam,eggs,ham".split(","))
#-- List Functions
nums = [55,44,33,22,11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
if any([i % 2 == 0 for i in nums]):
    print("At least on is even")
for v in enumerate(nums):
    print(v)
#-- Text Analyzer
#filename = input("Enter a filename:")
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

#filename = input("Enter a filename: ")
with open("filename.txt") as f:
  text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))
# Functional Programming 函数式编程？
print('--------------------------Functional Programming---------------------')
#--Introduction
def apply_twice(func,arg):
    return func(func(arg))
def add_five(x):
    return x + 5
print(apply_twice(add_five,10))
#--Pure Functions
def pure_funciton(x,y):
    temp = x + 2 * y
    return temp / (2 * x + y)
some_list = []
def impure(arg):
    some_list.append(arg)
#-- Lambdas
def my_func(f,arg):
    return f(arg)
my_func(lambda x:2 * x * x , 5 )
#named Functions
def polynomial(x):
    return x ** 2 + 5 * x + 4
print(polynomial(-4))
#Lambdas
print((lambda x: x ** 2 + 5 * x + 4)(-4))
double = lambda x: x * 2
print(double(7))
#--map & filter
def add_five(x):
    return x + 5
nums = [11,22,33,44,55,66]
result = list(map(add_five,nums))
print(result)
#nums = [11,22,33,44,55,66]
result = list(map(lambda x: x + 5,nums))
print(result)
#filter
result = list(filter(lambda x: x % 2 == 0,nums))
print(result)
#Generators
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))
#Decorators
def decor(func):
    def wrap():
        print("==========")
        func()
        print("==========")
    return wrap
def print_text():
    print("Hello world!")
decorated = decor(print_text)
decorated()

@decor
def print_text():
    print("Hello Joey!")
#Recursion
def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)
print(fatorial(5))
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)
print(is_odd(17))
print(is_even(23))
def fib(x):
    if x==0 or x ==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))
#Sets
num_set = {1,2,3,4,5,6}
word_set = set(["spam","eggs","sausage"])
print(3 in num_set)
print("spam" not in word_set)
nums = {1,2,3,4,1,4,5,6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
#itertools
from itertools import count
for i in count(3):
    print(i)
    if i>=11:
        break
from itertools import takewhile
#nums = list(accumulate(range(8)))
#print(nums)
print(list(takewhile(lambda x: x<=6,nums)))
from itertools import product,permutations
letters = ("A","B")
print(list(product(letters,range(2))))
print(list(permutations(letters)))
a = {1,2}
print((list(product(range(3),a))))
def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x,y-1)
print(power(2,3))
# Object-Oriented Programming 面向对象编程
print('--------------------------Object-Oriented Programming---------------------')
#Classes 类
class Cat:
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs

    def bark(self):
        print("Woof!")
felix = Cat("ginger",4)
rover = Cat("dog-Colored",4)
stumpy = Cat("Brown",3)
#__init__
print(felix.color)
felix.bark()
#Inheritance 继承
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def bark(self):
        print("Animal")
class Cat(Animal):
    def purr(self):
        print("Purr...")
class Dog(Animal):
    def bark(self):
        print("woof!")
fido = Dog("Fido","brown")
print(fido.color)
fido.bark()
#Magic Methods & Operator Overloading
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5,7)
second = Vector2D(3,9)
result = first + second
print(result.x)
print(result.y)
class SpecialString:
    def __init__(self,cont):
        self.cont  = cont
    def __truediv__(self,other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont,line,other.cont])

    def __gt__(self,other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)
spam = SpecialString("spam")
eggs = SpecialString("eggs")
hello = SpecialString("hello world!")
print(spam.__truediv__(hello))
#print(spam / hello) python2不支持？
spam > eggs
import random
class VagueList:
    def __init__(self,cont):
        self.cont = cont

    def __getitem__(self,index):
        return self.cont[index + random.randint(-1,1)]

    def __len__(self):
        return random.randint(0,len(self.cont)*2)
vague_list = VagueList(["A","B","C","D","F","G"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
#Object Lifecycle
#Data Hiding
class Queue:
    def __init__(self,contents):
        self._hiddenlist = list(contents)
    def push(self,value):
        self._hiddenlist.insert(0,value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
    __egg = 7
queue = Queue([1,2,3])
print(queue)
queue.push(0)
queue.pop()
print(queue)
print(queue._hiddenlist)
#print(queue.__egg)
# Class & Static Methods
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculator_area(self):
        return self.width * self.height
    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)
squre = Rectangle.new_square(5)
print(squre.calculator_area())
class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pinaeapples!")
        else:
            return True
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            self._pineapple_allowed = value
        else:
            raise ValueError("Alert! Intruder!")

ingredients = ["cheese","onions","spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
    print(pizza.toppings)
# Properties 属性
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
# Regular Expressions
print('--------------------------Regular Expressions---------------------')
# Introduction
import re
pattern = r"pam"
if re.match(pattern,"spamspamspam"):
    print("Match")
else:
    print("No Match")
match = re.search(pattern,"eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
# Search & Replace
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern,"Amy",str)
print(newstr)
#Simple Metacharacters
pattern = r"gr.y"
if re.match(pattern,"grey"):
    print("Match1")
if re.match(pattern,"gray"):
    print("Match2")
if re.match(pattern,"blue"):
        print("Match3")
pattern = r"^gr.y$"
if re.match(pattern,"grey"):
    print("Match1")
if re.match(pattern,"gray"):
    print("Match2")
if re.match(pattern,"grgray"):
        print("Match3")
#Character Classes
pattern = r"[aeiou]"
if re.search(pattern,"grey"):
    print("Match1")
if re.search(pattern,"qwertyuiop"):
    print("Match2")
if re.search(pattern,"rhythm myths"):
    print("Match3")
pattern = r"[A-Z][G-P][0-9]"
if re.search(pattern,"LS8"):
    print("Match1")
if re.search(pattern,"E3"):
    print("Match1")
if re.search(pattern,"1ab"):
    print("Match3")
pattern = r"[^A-Z]"
if re.search(pattern,"this is all quiet"):
    print("Match1")
if re.search(pattern,"AbCdEfG123"):
    print("Match2")
if re.search(pattern,"THISISALLSHOUTING"):
    print("Match3")
pattern = r"egg(spam)*"
if re.match(pattern,"egg"):
    print("Match5")
if re.match(pattern,"eggspamspamegg"):
    print("Match6")
if re.match(pattern,"spam"):
    print("Match7")
pattern = r"g+"
if re.match(pattern,"g"):
    print("Match5")
if re.match(pattern,"gggggggggg"):
    print("Match6")
if re.match(pattern,"abc"):
    print("Match7")
pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
   print("Match 1")
if re.match(pattern, "icecream"):
   print("Match 2")
if re.match(pattern, "sausages"):
   print("Match 3")
if re.match(pattern, "ice--cream"):
   print("Match 4")
pattern = r"9(1,3)$" #"9{1,3}$" matches string that have 1 to 3 nines.
if re.match(pattern,"9"):
    print("match1")
if re.match(pattern,"999"):
    print("match2")
if re.match(pattern,"9999"):
    print("match3")
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern,"abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern,"abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())
#Special Sequences
pattern = r"(.+) \1"
match = re.match(pattern, "word word")
if match:
   print ("Match 1")
match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")
match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")
pattern = r"(\D+\d)"
match = re.match(pattern, "Hi 999!")
if match:
   print("Match 1")
match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")
match = re.match(pattern, " ! $?")
if match:
    print("Match 3")
# Email 获取
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"
match = re.search(pattern, str)
if match:
   print(match.group())
#Pythonicness & Packaging
print('--------------------------Pythonicness & Packaging---------------------')
# The Zen of Python Python之道
import this
"""
Beautiful is better than ugly.
# 优美胜于丑陋（Python以编写优美的代码为目标）
Explicit is better than implicit.
# 明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
Simple is better than complex.
# 简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
Complex is better than complicated.
# 复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
Flat is better than nested.
# 扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
Sparse is better than dense.
# 间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
Readability counts.
# 可读性很重要（优美的代码是可读的）
Special cases aren't special enough to break the rules.
Although practicality beats purity.
# 即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
Errors should never pass silently.
Unless explicitly silenced.
# 不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写except:pass风格的代码）
In the face of ambiguity, refuse the temptation to guess.
# 当存在多种可能，不要尝试去猜测
There should be one-- and preferably only one --obvious way to do it.
# 而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
Although that way may not be obvious at first unless you're Dutch.
# 虽然这并不容易，因为你不是 Python 之父（这里的Dutch是指Guido）
Now is better than never.
Although never is often better than *right* now.
# 做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
# 如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
Namespaces are one honking great idea -- let's do more of those!
# 命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
PEP8: Python编码规范(PEP8: Style Guide for Python Code)

空格和缩进
    空格和缩进(WhiteSpace and Indentation)
    空格和缩进在Python语言中非常重要，它替代了其他语言中{}的作用，用来区分代码块和作用域。在这方面PEP8有以下的建议：
1、每次缩进使用4个空格
2、不要使用Tab，更不要Tab和空格混用
3、两个方法之间使用一个空行，两个Class之间使用两个空行
4、添加一个空格在字典、列表、序列、参数列表中的“，“后，以及在字典中的”：“之后，而不是之前
5、在赋值和比较两边放置一个空格（参数列表中除外）
6、紧随括号后面或者参数列表前一个字符不要存在空格

"""
#Pythonicness & Packaging
#Function Arguments
def function(named_arg,*args):
    print(named_arg)
    print(args)
function(1,2,3,4,5,6)
#Default Values
def function(x,y,food="spam"):
    print(food)
function(1,2)
function(3,4,"egg")
#keyword Arguments
def my_fucn(x,y=7,*args,**kwargs):
    print(kwargs)
my_fucn(2,3,4,5,6,a=7,b=8)
#Tuple Unpacking
numbers = (1,2,3)
a,b,c = numbers
print(a)
print(b)
print(c)
#a,b,*c,d = [1,2,3,4,5,6,7,8,9]
#此出语法Python2 环境下是错误的
