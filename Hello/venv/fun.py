#!/usr/bin/python
#coding=utf-8;
def printinfo( name = "default", age = 0 ):
   "打印任何传入的字符串"
   print("Name: ", name)
   print("Age ", age)

printinfo("zhangling",29)
printinfo()


def printargs (arg1, *vartuple ):
   "打印任何传入的参数"
   print(arg1)
   for var in vartuple:
       print(var)
printargs(0)
printargs(0,"arg1",["arg2",0])