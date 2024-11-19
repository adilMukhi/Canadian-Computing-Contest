"""
Canadian Computing Competition: 2024 Stage 1, Junior #2
Dusa eats Yobis, but only Yobis of a certain size.

If Dusa encounters a Yobi that is smaller than itself, it eats the Yobi, and absorbs its size. For example, if Dusa is of size 
 and it encounters a Yobi of size 
, Dusa eats the Yobi and expands to size 
.

If Dusa encounters a Yobi that is the same size as itself or larger, Dusa runs away without eating the Yobi.

Dusa is currently facing a line of Yobis and will encounter them in order. Dusa is guaranteed to eventually encounter a Yobi that causes it to run away. Your job is to determine Dusa's size when this happens.



Input Specification
The first line of input contains a positive integer, 
, representing Dusa's starting size.

The remaining lines of input contain positive integers representing the sizes of the Yobis in order.

Output Specification
Output the positive integer, 
, which is Dusa's size when it eventually runs away.
"""

d = int(input()) #dusa
while True:
    r = int(input()) #yobi
    if r < d:
        d = d + r
    else:
        print(d)
        break