### Problem 29 from Project Euler
#https://projecteuler.net/archives
"""How many distinct terms are in the sequence generated by
 ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?"""

distinct_number = []
a_min = 2
a_max = 100
b_min = 2
b_max = 100
for a in range(a_min, a_max+1):
    for b in range(b_min, b_max+1):
        num = a**b
        if num not in distinct_number:
            distinct_number.append(num)
print(len(distinct_number))
