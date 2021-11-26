class CSVFile():

	# Costruttore con il parametro nome
	def __init__(self, name):
		self.name = name
	
	def get_data(self):

		# Apro il file, sfruttando l'attributo nome
		my_file = open(self.name, 'r')

		# Inizializzo la lista da ritornare
		data=[]

		# Scorro tra tutte le righe del file
		for line in my_file:
			
			# Salto alla prossima iterazione nel caso ci sia la parola Date nella riga
			if 'Date' in line:
				continue

			# Utilizzo il metodo rstrip per rimuovere lo \n a fine riga
			line = line.rstrip()

			# Eseguo lo split della linea e la inserisco nella lista
			data.append(line.split(','))
		
		my_file.close()

		# Ritorno il risultato
		return data

# Istanzio un oggetto della classe CSVFile
my_csv_file = CSVFile('files/shampoo_sales.csv')
print(my_csv_file.get_data())