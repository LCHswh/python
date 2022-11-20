#lecture 4

#斐波那契数列
# def fib(n):
#     pred,curr = 0,1
#     while n > 1:
#         # temp = curr
#         # curr = curr + pred
#         # pred = temp
#         pred,curr = curr,pred + curr  #多赋值
#         n -= 1
#     return curr
# print(fib(8))


# from math import pi , sqrt
# def area_circle(r):
#     return pi * r * r

# def area_hexagon(r):
#     return r * r * sqrt(3) / 2

# def area(r,shape_constant):
#     assert r > 0,'A length must be positive'
#     return r * r * shape_constant

# #泛化实现 共有的部分 更简洁的实现
# def square(r):
#     return area(r,1)
#
# def circle(r):
#     return area(r,pi)
#
# def hexagon(r):
#     return area(r,3*sqrt(3)/2)


# def sum_naturals(n):
#     """_summary_
#     Args:
#         n(int): n>=0
#     >>> sum_naturals(5)
#     15
#     """
#     res,i= 0,1
#     while(i<=n):
#         res += i
#         i += 1
#     return res
#
# from operator import  mul
# def natual(i):
#     return i
#
# def cube(i):
#     return i*i*i
#
# def split_term(i):
#     return 8/mul(4*i-3,4*i+1)
#
# def summation(n,term):
#     res,i = 0,1
#     while i <= n:
#         res += term(i)
#         i += 1
#     return res
#
# print(summation(5,cube))

#function as return values
#高阶函数
# def make_adder(n):
#     def adder(k):
#         return n+k
#     return adder


#lambda expression 重要但不常用
#lambda 形参 ：返回表达式
# func = lambda a , b : a*b
# print(func(1,2))


#if控制语句
# def condition():
#     print("THIS IS CONDITION")
#     return True
#
# def if_suite():
#     print("suite")
#
# def else_suite():
#     print("else_suite")

# and 从左至右，当 当前数 为0的时候，返回当前数
# or 从左至右 当 当前数为 1 的时候，返回当前数
# print(1 and 2 and False)
# print(0 or False or 3)

#<consequent> if <predicate> else <alternative>
# 如果<predicate>是True 返回<consequent>, False返回<alternative>
# from math import fabs
# def frac_abs(x):
#     if x == 0:
#         return 0
#     else:
#         return fabs(1/x)
# print(frac_abs(10))

