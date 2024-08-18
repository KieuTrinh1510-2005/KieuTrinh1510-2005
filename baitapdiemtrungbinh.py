# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:39:55 2024

@author: Student
"""

a = float(input("Nhập điểm trung bình học lực(GPA)"))
if a < 3.5:
    print("Học lực Kém")
elif 3.5 <= a < 5.0:
    print("Học lực Yếu")
elif 5.0 <= a < 7.0:
    print("Học lực Trung Bình")
elif 7.0 <= a < 8.0:
    print("Học lực Khá")
elif 8.0 <= a < 9.0:
    print("Học lực Gioi")
elif 9.0 <= a <=10:
    print("Học lực Xuất sắc")
else:
    print("Không xác định")
    
    