# _*_ coding: utf-8 _*_
# Base Concepts 基础概念
print('---------------------------------Base Concepts-----------------------------')
print('Hello World!')
#--quit() 退出控制台

print("\n")
# Control Structures 控制流
print('-------------------------------Control Structures---------------------------')
#   List 集合
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
#   List Functions 集合函数
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
#   Range 范围
numbers = list(range(10))
print(numbers)
numbers = list(range(3,8))
print(numbers)
print(range(20) == range(0,20))
numbers = list(range(5,20,2))
print(numbers)
#   For Loop
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
