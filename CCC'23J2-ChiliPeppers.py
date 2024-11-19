"""
CCC '23 J2 - Chili Peppers Canadian Computing Competition: 2023 Stage 1, Junior #2 
Ron is cooking chili using an assortment of peppers. The spiciness of a pepper is 
measured in Scoville Heat Units (SHU). Ron's chili is currently not spicy at all, 
but each time Ron adds a pepper, the total spiciness of the chili increases by the SHU
 value of that pepper. The SHU values of the peppers available to Ron are shown in the 
 following table: Pepper Name Scoville Heat Units 1500 6000 Poblano Mirasol Serrano 15500
   Cayenne Thai 40000 Habanero 75000 125000 CONTESTS Your job is to determine the total 
   spiciness of Ron's chili after he has finished adding peppers. Input Specification The
     first line of input will contain a positive integer N, representing the number of 
     peppers Ron adds to his chili. The next N lines will each contain the name of a pepper 
     Ron has added. Each pepper name will exactly match a name that appears in the table above. 
     Note that more than one pepper of the same name can be added. Output Specification 
     The output will consist of a positive integer T, representing the total spiciness of Ron's chili.
"""

numPeppers = int(input())
totalSpiciness = 0
for i in range(numPeppers):
    pepper = input()
    if pepper == 'Poblano':
        totalSpiciness += 1500
    elif pepper == 'Mirasol':
        totalSpiciness += 6000
    elif pepper == 'Serrano':
        totalSpiciness += 15500
    elif pepper == 'Cayenne':
        totalSpiciness += 40000
    elif pepper == 'Thai':
        totalSpiciness += 75000
    elif pepper == 'Habanero':
        totalSpiciness += 125000

print(totalSpiciness)