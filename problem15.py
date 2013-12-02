# -*- coding: utf-8 -*-
# Problem 15 - Lattice Paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Para resolver esse problema, imaginemos uma matriz 2D com 1 entrada pra cada vértice do "lattice", ou seja, n+1.
# essa matriz será "dobrada" diagonalmente do destino até a origem, e as somas serão computadas pra cada um dos vértices.

import getopt, sys

def lattice_paths(size, debug=False):
	l = [1] # this is the base lattice 1x1
	while size >= len(l):
		l = [ a+b for a,b in zip([0]+l,l+[0]) ]
	while len(l)>1:
		l = [ a+b for a,b in zip([0]+l,l+[0]) ]
		l = l[1:-1]
	return l[0]

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], "g:")
	except getopt.GetoptError as err:
		# print help information and exit:
		print(err) # will print something like "option -a not recognized"
		print 'please inform the grid size with the -g option'
		sys.exit(2)
	
	for o, a in opts:
		if o == "-g":
			size = int(a)
	
	print 'There are %s paths in a %sx%s lattice' % (lattice_paths(size), size, size)
