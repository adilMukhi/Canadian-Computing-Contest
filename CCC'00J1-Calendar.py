"""
Canadian Computing Competition: 2000 Stage 1, Junior #1
Write a program to print out a calendar for a particular month given
 the day on which the first of the month occurs together 
 with the number of days in the month.

Your program should take as input an integer representing the
 day of the week on which the month begins (1 for Sunday, 2 for Monday, …,
   7 for Saturday), and an integer which is the number of days in the month 
   (between 28 and 31 inclusive). Your program should print the appropriate 
   calendar for the month. You can assume that all input data will be valid.

DMOJ-specific note: None of the output lines should contain trailing whitespace.
 The last line must end with a newline.
"""

start = int(input())
end = int(input())
print("Sun Mon Tue Wed Thr Fri Sat")
day = 1

