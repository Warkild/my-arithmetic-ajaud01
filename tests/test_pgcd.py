from my_arithmetic_ajaud01.pgcd import pgcd

def test_pgcd():

	# Simple case
	assert pgcd(60, 48) == 12
	assert pgcd(7, 5) == 1
	assert pgcd(0, 10) == 10
	
	# Limit case
	assert pgcd(1, 1) == 1
	assert pgcd(1, 2) == 1
	assert pgcd(2, 1) == 1
	assert pgcd(2, 2) == 2
