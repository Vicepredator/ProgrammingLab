import datetime

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

	# Costruttore con il parametro nome
	def __init__(self, name = None):
		
		# Controllo se il nome del file e' una stringa
		if type(name) is not str:
			raise ExamException('[ERROR] ~ File name should be a string')
		else:
			# Assegno il nome del file ad un attributo della classe
			self.name = name

	# Classe per ottenere i dati da file CSV pronti per essere usati dalla funzione detect_similar_monthly_variations
	def get_data(self):

		# Variabile per salvare i mesi passati, in modo da controllare non ci siano doppioni
		dates = []

		# Apro il file, sfruttando l'attributo nome
		try:
			my_file = open(self.name, 'r')
		except:
			raise ExamException('[ERROR] ~ Error while trying to read the file.')
		# Inizializzo la lista da ritornare
		data=[]

		# Scorro tra tutte le righe del file
		for i,line in enumerate(my_file):

			# Utilizzo il metodo rstrip per rimuovere lo \n a fine riga poi separo i valori con la virgola
			values = line.rstrip().split(',')

			# Controllo se la linea ha 2 elementi, se no la considero inconpleta e la salto
			if len(values) < 2:
				# Stampo un messaggio
				print('[WARNING] ~ Skipped line {} with content: {} due to missing data'.format(i+1,values))
				continue
			
			# Rimuovo qualsiasi altro valore non necessario
			values = values[:2]

			# Trasformo il numero di passeggeri da stringa ad intero

			## Uso un try catch per saltare la riga nel caso non sia un numero
			## Automaticamente verra' saltata anche la prima riga di intestazione
			try:
				values[1] = int(values[1])
			except:
				print('[WARNING] ~ Skipped line {} due to string to int conversion of {}'.format(i+1,values[1]))
				continue

			# Controllo che i passeggeri non siano nulli o negativi
			if values[1] <= 0:
				print('[WARNING] ~ Skipped line {} due to negative or null value of {}'.format(i+1,values[1]))
				continue
			
			# Controllo se le date sono valide e se non sono duplicate
			try:
			
				curr_date = datetime.datetime.strptime(values[0], '%Y-%m')

				if curr_date in dates:
					raise ExamException('[ERROR] ~ Duplicated date at line {}'.format(i+1))
			
				if len(dates) > 0:
					if curr_date <= dates[len(dates)-1]:
						raise ExamException('[ERROR] ~ Untidy date at line {}'.format(i+1))

				dates.append(curr_date)
			except ValueError:
				print('[WARNING] ~ Skipped line {} due to string to date conversion of {}'.format(i+1,values[0]))
				continue
			# Eseguo lo split della linea e la inserisco nella lista
			data.append(values)
		
		my_file.close()

		if len(data) == 0:
			raise ExamException('[ERROR] ~ File should contain at least one valid line')
		# Ritorno il risultato
		return data

# Funzione che ritorna un arrai contenente dei booleani che indicano se la variazione per coppia di mese nei rispettivi anni e' miore o uguale a 2
def detect_similar_monthly_variations(time_series, years):

	# Dichiaro le variabili
	first_year = []
	second_year = []
	results = []

	# Estraggo dalla lista gli elementi degli anni che mi interessano
	for element in time_series:

		# Converto le date in oggetti datetime, per comodita' di utilizzo
		element[0] = datetime.datetime.strptime(element[0], '%Y-%m')

		# Metto i dati del mese in questione in una lista per ogni anno
		if element[0].year == years[0]:
			first_year.append(element)
		elif element[0].year == years[1]:
			second_year.append(element)

	# Controllo se la selezione degli anni esiste nella lista time_series
	if len(first_year) == 0 or len(second_year) == 0:
		raise ExamException('[ERROR] ~ Invalid year selection')

	# Per ogni mese mi salvo in 2 liste le coppie di valori relativi al mese che sto controllando
	for i in range(1,12):
		try:
			couple_month_first_year = [list(filter(lambda el : el[0].month == i, first_year))[0], list(filter(lambda el : el[0].month == i+1, first_year))[0]]
			couple_month_second_year = [list(filter(lambda el : el[0].month == i, second_year))[0], list(filter(lambda el : el[0].month == i+1, second_year))[0]]
		except IndexError:

			# Questa eccezione viene scatenata se non esiste un valore per un determinato mese
			results.append(False)
			continue
		
		# Calcolo la differenza tra la coppia di mesi del primo anno e del secondo
		delta = abs((couple_month_first_year[0][1] - couple_month_first_year[1][1]) - (couple_month_second_year[0][1] - couple_month_second_year[1][1]))
		
		# Se la differenza di mesi e' minore o uguale a 2 siamo nel range richiesto e ritorno True altrimenti False
		if(delta <= 2):
			results.append(True)
		else:
			results.append(False)

	return results