# -*- coding: iso-8859-1 -*-

# Finn antal tecken i rad

import numpy as np

def finn_rad(matris, tecken, antal):
	"""Undersöker antal tecken i rad"""
	a = 0
	for vek in matris:
		for i in vek:
			if i == tecken:
				a += 1
			else:
				a = 0
			if a == antal:
				return True
	return False

def finn_kolumn(matris, tecken, antal):
	"""Transponerar matris och undersöker förekomsten av 
	önskat tecken"""
	a = 0
	matris = [list(i) for i in zip(*matris)]
	for vek in matris:
		for i in vek:
			if i == tecken:
				a += 1
				#print(a)
			else:
				a = 0
			if a == antal:
				return True
	return False

def finn_diagonal(matris, tecken, antal):
	"""Förskjuter matris så att vänsterupp-till-högerner och
	högerupp-till-vänsterner diagonaler blir listor"""
	np_matris = np.asarray(matris)
	m = np_matris.shape[0]		#antal rader
	n = np_matris.shape[1]		#antal kolumner
	diags = [np_matris[::-1,:].diagonal(i) for i in range(-m+1,n)]
	diags.extend(np_matris.diagonal(i) for i in range(n-1,-m,-1))
	#print (diags)
	for vek in diags:
		#print(vek)
		a = 0
		for i in vek:
			if i == tecken:
				a += 1
				#print(a)
			else:
				a = 0
			if a == antal:
				return True
	return False



if __name__ == '__main__':
	m1 = [['X', 'O', '-'] , ['X', 'X', 'O'], ['X', '-', 'X']]
	m2 = [['O', 'O', 'O'] , ['O', '-', 'X'], ['X', 'X', 'O']]
	print('')

	# Fall A: då 3 'x' ska hittas i rad
	utfall = finn_rad(m1,'X', 3)
	print'3 X i rad för matris = '
	print m1[0]
	print m1[1]
	print m1[2]
	print'Förväntat värde är False'
	print 'Utfall: ' ,utfall
	print('')

	# Fall A: då 3 'x' ska hittas i kolumn
	utfall = finn_kolumn(m1,'X', 3)
	print'3 X i kolumn för matris = '
	print m1[0]
	print m1[1]
	print m1[2]
	print'Förväntat värde är True'
	print 'Utfall: ' ,utfall
	print('')

	# Fall A: då 3 'x' ska hittas i diagonal
	utfall = finn_diagonal(m1,'X', 3)
	print'3 X i diagonal för matris = '
	print m1[0]
	print m1[1]
	print m1[2]
	print'Förväntat värde är True'
	print 'Utfall: ' ,utfall
	print('')

	# Fall B: då 3 'O' ska hittas i rad
	utfall = finn_rad(m2,'O', 3)
	print'3 O i rad för matris = '
	print m2[0]
	print m2[1]
	print m2[2]
	print'Förväntat värde är True'
	print 'Utfall: ' ,utfall
	print('')

	# Fall B: då 3 'O' ska hittas i kolumn
	utfall = finn_kolumn(m2,'O', 3)
	print'3 O i kolumn för matris = '
	print m2[0]
	print m2[1]
	print m2[2]
	print'Förväntat värde är False'
	print 'Utfall: ' ,utfall
	print('')

	# Fall B: då 3 'O' ska hittas i diagonal
	utfall = finn_diagonal(m2,'O', 3)
	print'3 O i diagonal för matris = '
	print m2[0]
	print m2[1]
	print m2[2]
	print'Förväntat värde är False'
	print 'Utfall: ' ,utfall
	print('')
	print('_________________________________')