"""
Canadian Computing Competition: 2024 Stage 1, Junior #3
After completing a competition, you are struck with curiosity. How many participants were awarded bronze level?

Gold level is awarded to all participants who achieve the highest score. Silver level is awarded to all participants who achieve the second highest score. Bronze level is awarded to all participants who achieve the third highest score.

Given a list of all the scores, your job is to determine the score required for bronze level and how many participants achieved this score.



Input Specification
The first line of input contains a positive integer, 
, representing the number of participants.

Each of the next 
 lines of input contain a single integer representing a participant's score.

Each score is between 
 and 
 (inclusive) and there will be at least three distinct scores.

The following table shows how the available 15 marks are distributed:

Marks	Description	Bound
6	The scores are distinct and the number of participants is small.	
7	The scores might not be distinct and the number of participants is small.	
2	The scores might not be distinct and the number of participants could be large.	
Output Specification
Output a non-negative integer, 
, and a positive integer, 
, separated by a single space, where 
 is the score required for bronze level and 
 is how many participants achieved this score.
"""

# IDK