"""
Canadian Computing Competition: 2024 Stage 1, Junior #1
There is a new conveyor belt sushi restaurant in town. Plates of sushi travel around the restaurant on a raised conveyor belt and customers choose what to eat by removing plates.

Each red plate of sushi costs 
, each green plate of sushi costs 
, and each blue plate of sushi costs 
.



Your job is to determine the cost of a meal, given the number of plates of each colour chosen by a customer.

Input Specification
The first line of input contains a non-negative integer, 
, representing the number of red plates chosen. The second line contains a non-negative integer, 
, representing the number of green plates chosen. The third line contains a non-negative integer, 
, representing the number of blue plates chosen.

Output Specification
Output the non-negative integer, 
, which is the cost of the meal in dollars.
"""

r = int(input())
g = int(input())
b = int(input())

total = r*3 + g*4 + b*5

print (f"{total}")