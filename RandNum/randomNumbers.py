'''Program that generates a random number in range from 0 to 100 and asks user to guess it. In case of fail it asks again.'''

import random

generatedRand = (random.randint(0,100)) #generation of random number in range from 0 to 100 and 1st question for chosenNumber 
chosenNumber = input("Zgaduj! Wybierz liczbę z zakresu 0-100: ") #ask user to guess the number for the 1st time

def number(): #function that asks user every next time he/she fails
	global chosenNumber 
	chosenNumber =  input("Wybierz następną liczbę: ")
	exceptionHandling()

def exceptionHandling(): #checking if typed value is correct
	global chosenNumber
	try:
		if float(chosenNumber).is_integer() == True:
			if int(chosenNumber) < 0 or int(chosenNumber) > 100:
				print("Musisz wpisać liczbę, która zawiera się w zadanym zakresie.")
				number()
		else:
			print("Podawane liczby muszą należeć do zbioru liczb całkowitych.")
			number()
	except ValueError:
		print("Znaki inne niż cyfry nie są dozwolone.")
		number()	

def mainloop():
	exceptionHandling()
	while int(chosenNumber) != generatedRand: #main loop
		if int(chosenNumber) > generatedRand:
			smallerOrBigger = 'mniejsza!'
		else:
			smallerOrBigger = 'większa!'
		print('To nie ta liczba! Liczba której poszukujesz jest {}'.format(smallerOrBigger))
		number()
	print('Brawo! Wygrałeś talon! Koniec programu.')

try:
	mainloop()
except:
	print('Wystąpił nieznany błąd.')
	raise
