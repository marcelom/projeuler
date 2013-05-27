# -*- coding: utf-8 -*-
"""Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

# Existe um padrão... vou tentar resolver sem a força bruta...
# ele é o seguinte: o próximo bloco sempre será o resultado do anterior + (n-1)

ds = { 1:1 }

for a in range(3, 1001 + 1, 2):
	ds[a] = ds[a - 2] + 4 * (a - 2) * (a - 2) + 10 * (a - 1)
	# print ds[a]

print ds[1001]
