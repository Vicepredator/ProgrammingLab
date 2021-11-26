# ===========
# Un primo approccio a Python
# ===========

def stampa(list):
	print(list)

def statistiche(list):
	
	#Definisco le variabili
	sum = 0

	# Controllo che tutti gli elementi della lista siano interi
	if not all(type(el) == int for el in list):
		# Se non sono interi stampo un errore e ritorno 0
		print('You must use a list of int')
		return 0,0,0,0

	# Inizializzo i valori di min e max per poter fare i controlli dopo
	# Li inizializzo al primo valore della lista
	min = max = list[0]

	# Ciclo tra tutti gli elementi della lista per calcolare somma, minimo e massimo
	for i, el in enumerate(list):
		
		# Sommo l'n-esimo valore
		sum += el
		
		# Controllo se l'n-esimo valore è min o max
		if el > max: 
			max = el
		
		if el < min:
			min = el

	# Con la somma precedentemente calcolata mi calcolo la media sfruttando la funzione len() che mi ritorna il numero di elmenti della lista
	avg = sum / len(list)

	return sum, avg, min, max


def somma_vettoriale(list1, list2):
	
	# Controllo che le 2 liste abbiano la stessa lunghezza, altrimenti stampo un errore e ritorno []
	if len(list1) != len(list2):
		print('Le 2 liste devono avere la stessa dimensione')
		return []

	# Controllo che tutti gli elementi delle liste siano interi, altrimenti stampo un errore e ritonto []
	# Osservazione: Utilizzo la funzione zip che mi permette di ciclare su 2 liste contemporaneamente, il for mi ritornerà 2 valori contemporaneamente, in questo caso 'a' e 'b'
	if not all(type(a) == int and type(b) == int for a,b in zip(list1,list2)):
		print('Le liste devono contenere solo interi')
		return []

	# Inizializzo la lista che poi conterrà le somme vettoriali
	list = []

	# Calcolo le somme vettoriali sfruttando il metodo zip()
	for a,b in zip(list1,list2):
		list.append(a+b)
	
	return list
	

# Test del programma

lista = [1,2,3,12,4]
lista1 = [172,4,12,3,5]

stampa(lista)

sum, avg, min, max = statistiche(lista)

print("Sum: {}\nAvg: {}\nMin: {}\nMax: {}".format(sum, avg, min, max))

print(somma_vettoriale(lista,lista1))