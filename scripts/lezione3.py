# Programma per sommare i valori delle vendite di shampoo salvare nel file shampoo_sales.csv

# Apro il file
shampoo_sales = open('files/shampoo_sales.csv', 'r')

#Inizializzo la variabile somma
somma = 0

#Leggo tutte le righe e sommo il valore di value
for line in shampoo_sales:

	# Faccio lo split di ogni riga sulla virgola
	elements = line.split(',')

	# Distinguo il caso in cui sia la prima riga
	if elements[0] != 'Date':

		# Setto la data e il valore
		date = elements[0]
		value = elements[1]
		# Aggiungo alla lista dei valori questo valore
		somma += float(value)

#Stampo il risultato e utilizzo la funzione round per troncare a 3 cifre decimali
print('La somma delle vendite è {}'.format(round(somma, 3)))