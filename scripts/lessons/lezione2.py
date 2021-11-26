def sum_list(the_list):
	sum = 0
	for item in the_list:
		sum += item
	return sum

numbers = [1,5,36,7,3,9,34]

print('La somma è {}'.format(sum_list(numbers)))