import sys

class CSVFile():

	# Costruttore con il parametro nome
	def __init__(self, name):
		self.name = name

		# Gesticsco il caso in cui non esista un file con il nome dato
		try:
			# Apro il file, sfruttando l'attributo nome
			my_file = open(self.name, 'r')
			my_file.close()
		except:
			print('Il file "{}" non esiste!'.format(self.name))
			sys.exit()
	
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

class NumericalCSVFile(CSVFile):

	# Overloading della funzione get_data() nella classe CSVFile
	def get_data(self):

		# Dalla classe CSVFile ottengo la lista come stringa che modifico dopo
		elements= super().get_data()

		data = []

		# Scorro tra tutte le righe del file
		for line in elements:

			# Nuova linea provvisoria
			newLine = [line[0]]

			# Ciclo tra tutti gli elementi della lista tranne il primo
			for element in line[1:]:
				
				# Gesticsco gli errori nella conversione in float
				try:
					element = float(element)
				except ValueError:
					# Gesticsco l'eccezione
					print('"{}" non può essere convertito a float\n Lo imposto a 0'.format(element))
					element = 0.0;
				
				# Aggiungo il valore alla nuova linea
				newLine.append(element)

			# Aggiungo la linea alla lista finale
			data.append(newLine)


		# Ritorno il risultato
		return data

# Istanzio un oggetto della classe CSVFile
my_csv_file = NumericalCSVFile('files/shampoo_sales.csv')

print(my_csv_file.get_data())