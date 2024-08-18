# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:36:42 2024

@author: Student
"""
a = float(input("Độ dài cạnh a: "))
b = float(input("Độ dài cạnh b: "))
c = float(input("Độ dài cạnh c: "))
if a + b > c and b + c > a and a + c > b:
        print(" a , b , c là 3 cạnh của tam giác ")
else:
        print(" a , b , c không là 3 cạnh của tam giác ")

