#!/usr/bin/python
#coding=utf-8;
# 以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
import fun

# 1、print print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
print("你好，python")
print("你好，python"),
print("你好，python")
# 2、True False
if True:
    print("True")
else:
    prin("False")
# 3、句子 段落
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print(word)
print(sentence)
print(paragraph)
# 4、数据结构
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday'] # 数组
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print(days)
print(counter)
print(miles)
print(name)
# 5、字符串
str = "hello python"
print(str)
print(str[0])
print(str[0:8])
print(str[2:8])
print(str[2:])
print(str + "+see")
print(str * 2)
print("My name is %s and weight is %d kg!" % ('Zara', 21))
# 6、列表
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
print(list)
print(list[0])
print(list[1:3])
print(list[0:])
print(list * 2)
# 7、元组 元组不能二次赋值，相当于只读列表。 元组是不允许更新的
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[0:])
# 8、字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
print(dict)
print(dict["one"])
print(dict.keys())
print(dict.values())

fun.printinfo()
fun.printargs("steven")

