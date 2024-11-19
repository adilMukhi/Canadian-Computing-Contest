"""
CCC '23 J3 - Special Event Canadian Computing Competition: 2023 Stage 1, Junior #3 
You are trying to schedule a special event on one of five possible days. Your job is
 to determine on which day you should schedule the event, so that the largest number
   of interested people are able to attend. Input Specification The first line of input 
   will contain a positive integer N, representing the number of people interested in 
   attending your event. The next N lines will each contain one person's availability using
one character for each of Day 1, Day 2, Day 3, Day 4, and Day 5 (in that order). 
The character Y means the person is able to attend and a period (.) means the person is
not able to attend. The following table shows how the available 15 marks are distributed:
 Marks Description 6 There will be exactly one day on which every person will be able
to attend. 6 There will be exactly one day on which the largest number of people will
be able to attend. 3 There might be more than one day on which the largest number
of people will be able to attend. Output Specification The output will consist of
one line listing the day number(s) on which the largest number of interested people 
are able to attend. If there is more than one day on which the largest number of people 
are able to attend, output all of these day numbers in increasing order and separated by
 commas (without spaces).
"""

numPpl = int(input())
days = [0, 0, 0, 0, 0]
for i in range(numPpl):
    line = input()
    for j in range(5):
        if line[j] == 'Y':
            days[j] += 1

max = 0
for i in range(5):
    if days[i] > max:
        max = days[i]
for i in range(5):
    if days[i] == max:
        print(i+1, end='')
        if i != 4:
            print(',', end='')