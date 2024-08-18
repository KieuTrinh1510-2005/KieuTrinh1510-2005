# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:05:44 2024

@author: Student
"""
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0: 
    if b == 0:
        print(" Phương trình vô số nghiệm ")
    else:
        print("Phương trình vô nghiệm ")
else:
    x = -b / a 
    print(" Nghiệm của phương trinh ax + b = 0 là ")
    
