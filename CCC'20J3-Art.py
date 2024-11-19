"""
CCC '20 J3 - Art Canadian Computing Competition: 2020 Stage 1, Junior #3 

Mahima has been experimenting with a new style of art. 
She stands in front of a canvas and, using her brush, flicks drops of paint onto the canvas. 
When she thinks she has created a masterpiece, she uses her 3D printer to print a frame to
surround the canvas. Your job is to help Mahima by determining the coordinates of the smallest
possible rectangular frame such that each drop of paint lies inside the frame. 

Points on the frame are not considered inside the frame. 
Input Specification The first line of input contains the number of drops of paint, N,
where 2 ≤ N ≤ 100 and N is an integer. Each of the next N lines contain 
exactly two positive integers X and Y separated by one comma (no spaces). 
Each of these pairs of integers represent the coordinates of a drop of paint on the canvas. 
Assume that X ≤ 100 and Y≤ 100, and that there will be at least two distinct points.
The coordinates (0, 0) represent the bottom-left corner of the canvas.
For 12 of the 15 available marks, X and Y will both be two-digit integers. 
Output Specification Output two lines. Each line must contain exactly two 
non-negative integers separated by a single comma (no spaces). The first line
represents the coordinates of the bottom-left corner of the rectangular frame.
The second line represents the coordinates of the top-right corner of the rectangular frame.
"""

n = int(input())
x, y = [], []
for i in range(n):
    a, b = input().split(", ")
    x.append(int(a))
    y.append(int(b))

print(f"{min(x)-1},{min(y)-1}")
print(f"{max(x)+1},{max(y)+1}")