# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:02:50 2024

@author: Student
"""


a = float(input("Số km di chuyển là "))
if a == 1:
    sotien = 20
    print("Số tiền phải trả là " , sotien ,"k")
elif 2 <= a <= 3:
    sotien = a*13
    print("Số tiền phải trả là " , sotien ,"k")
elif 4<= a <= 8:
    sotien = 12*(a-3)+3*13
    print("Số tiền phải trả là " , sotien ,"k")
else:
    sotien =3*13+5*12+(a-8)*10
    if sotien > 100:
        st = sotien*0.92
        print("Số tiền phải trả là " , st ,"k")
    else:
        print("Số tiền phải trả là " , sotien ,"k")
        