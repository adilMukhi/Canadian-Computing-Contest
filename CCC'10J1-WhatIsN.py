"""
CCC '10 J1 - What is n, Daddy? View as PDF Canadian Computing Competition: 2010 Stage 1, Junior #1 
Submit solution Natalie is learning to count on her fingers. When her Daddy tells her a number n 
(1 ≤ n ≤ 10), she asks "What is n, Daddy?", by which she means "How many fingers should I hold up
 on each hand so that the total is n?" To make matters simple, her Daddy gives her the correct finger 
 representation according to the following rules: All submissions Best submissions • the number may be
   represented on one or two hands; Voting statistics • if the number is represented on two hands, the
     larger number is given first. For example, if Natalie asks "What is 4, Daddy?", her Dad may reply: 
     Points: 3 • 4 is 4. Time limit: 2.0s • 4 is 3 and 1. Memory limit: 256M • 4 is 2 and 2. > Problem 
     type Your job is to make sure that Natalie's Daddy gives the correct number of answers. 
     Input Specification The input will be a single integer i such that 1 ≤ i ≤ 10. Output Specification
       The output is the number of ways of producing that number on two hands, subject to the rules 
       outlined above.
"""

n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
elif n == 4:
    print(2)
elif n == 5:
    print(2)
elif n == 6:
    print(3)
elif n == 7:
    print(3)
elif n == 8:
    print(4)
elif n == 9:
    print(4)
elif n == 10:
    print(5)