"""
CCC '14 J1 - Triangle Times Canadian Computing Competition: 2014 Stage 1, Junior #1 

You have trouble remembering which type of triangle is which. You write a program to help. 
Your program reads in three angles (in degrees). 

• If all three angles are 60, output Equilateral 
• If the three angles add up to 180 and exactly two of the angles are the same, output Isosceles 
• If the three angles add up to 180 and no two angles are the same, output Scalene 
• If the three angles do not add up to 180, output Error 
Input Specification The input consists of three integers, each on a separate line. Each integer will be greater than 0 and less than 180. 
Output Specification Exactly one of Equilateral Isosceles Scalene or Error will be printed on one line.
"""

a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a + b + c == 180 and (a == b or a == c or b == c):
    print("Isosceles")
elif a + b + c == 180 and (a != b and a != c and b != c):
    print("Scalene")
elif a + b + c != 180:
    print("Error")