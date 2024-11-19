"""
CCC '20 J2 - Epidemiology Canadian Computing Competition: 2020 Stage 1, Junior #2 
People who study epidemiology use models to analyze the spread of disease. 
In this problem, we use a simple model. When a person has a disease, they infect exactly
R other people but only on the very next day. No person is infected more than once. 
We want to determine when a total of more than P people have had the disease. 
(This problem was designed before the current coronavirus outbreak, and we acknowledge
the distress currently being experienced by many people worldwide because of this 
and other diseases. We hope that including this problem at this time highlights the 
important roles that computer science and mathematics play in solving real-world problems.)
    
Input Specification There are three lines of input. Each line contains one positive integer.
The first line contains the value of P. The second line contains N, the number of
people who have the disease on Day 0. The third line contains the value of R.
Assume that P < 107 and N < P and R ≤ 10. Output Specification Output the number
of the first day on which the total number of people who have had the disease is
greater than P.
"""

p, n, r = int(input()), int(input()), int(input())

total = n
day = 0
while total <= p:
    day += 1
    # The number of infected people is a geometric series where the coefficient
    # is N and the ratio is R.
    total += (r ** day) * n

print(day)