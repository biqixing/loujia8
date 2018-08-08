# #!/usr/bin/env python3
# #定义工资的变量  Salary  起征点 Point=3500
# #应纳税所得额 变量 Ratepaying_first
# #应纳税额 变量 Ratepaying   税率 Cess  扣除Deduction
 import sys
 try:
     Salary=int(sys.argv[1])
 except:
     print("Parameter Error")
 Point=3500
 Cess=[0.03,0.1,0.2,0.25,0.3,0.35,0.45]

 Deduction=[0,105,555,1005,2755,5505,13505]

 Ratepaying_first=Salary-Point

 if Ratepaying_first <=0:
     print("{0:.2f}".format(0))
 elif Ratepaying_first <=1500 and Ratepaying_first>0:
     Ratepaying = (Ratepaying_first * Cess[0]) - Deduction[0]
     print("{0:.2f}".format(Ratepaying))
 elif Ratepaying_first <=4500 and Ratepaying_first>1500:
     Ratepaying = (Ratepaying_first * Cess[1]) - Deduction[1]
     print("{0:.2f}".format(Ratepaying))
 elif Ratepaying_first <=9000 and Ratepaying_first >4500:
     Ratepaying = (Ratepaying_first * Cess[2]) - Deduction[2]
     print("{0:.2f}".format(Ratepaying))
 elif Ratepaying_first <=35000 and Ratepaying_first>9000:
     Ratepaying = (Ratepaying_first * Cess[3]) - Deduction[3]
     print("{0:.2f}".format(Ratepaying))
 elif Ratepaying_first <= 55000 and Ratepaying_first>35000:
     Ratepaying = (Ratepaying_first * Cess[4]) - Deduction[4]
     print("{0:.2f}".format(Ratepaying))
 elif Ratepaying_first <=80000 and Ratepaying_first>55000:
     Ratepaying = (Ratepaying_first * Cess[5]) - Deduction[5]
     print("{0:.2f}".format(Ratepaying))
 elif Ratepaying_first>80000:
     Ratepaying = (Ratepaying_first * Cess[6]) - Deduction[6]
     print("{0:.2f}".format(Ratepaying))
 else :
    print("This is None!")


def test(a):
    c=5-a
    if c>0:
        return(-c)
    else:
        return(c+1)

a=10
b=test(a)
print(b)
