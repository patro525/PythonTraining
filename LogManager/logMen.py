'''
Program:
- takes a valid email address and password or exit,
- allows to read the file "data.txt" and change a password,
- allows user to type a pattern word(s) that will be changed for some other word(s), also typed by user,
- saves the file "data.txt" and gives a choice to logout or make another word change.
'''
import re, os, stdiomask
'''
from pynput import keyboard
def escapePress(key):
	if key == keyboard.Key.esc:
		print('ESC Pressed!')
		menu()

with keyboard.Listener(on_press = escapePress) as l:
	pass
'''
def menu():
	print('---MENU---\nChose an option:\n1. Login\n2. Password change\n3. New user\n4. Exit')
	menuOption = input('')
	if menuOption == '1':
		login()
	elif menuOption == '2':
		passwdChange()
	elif menuOption == '3':
		addUser()
	elif menuOption == '4':
		exit()
	else:
		print('Wrong number. Try again.')
		menu()

def mail(): #takes an email address, checks if it is a valid one; if not - gives an info and asks to repeat
	address = input('Type your email address: ')
	match = re.search(r'^([\w.-]+)@([\w.-]+)$', address) #checking if it is a valid email address
	if match:
		global name, domain, line, currentUserName
		name = match.group(1)
		domain = match.group(2)
		passes = open('passes.txt', 'r') #opening of 'passes.txt' and search for 'name'	
		for i in passes:
			line = str(i)			
			currentUserName = re.search(name, line)
			currentUserDomain = re.search(domain, line)
			if currentUserName and currentUserDomain:
				print('Hello, {}!'.format(name))
				lineData = str(currentUserName.group())
				break
			else:
				lineData = '0'
		passes.close()
		passwd()
		if lineData == "0":
			print('There is no such user!')
			menu()
		else:
			pass 
	else:
		print('Invalid email address.')
		menu()

def passwd(): #takes a password and checks if it fits to the right user
	password = str(stdiomask.getpass())
	global correctPasswd
	correctPasswd = re.search(r';([\w.-]+)$', line)
	if correctPasswd.group(1) == password: #loop that check if it is correct
		print('Login was successfull.')
		menu()
	else:
		print('Access denied! Type correct password.')
		passwd()
	
def login(): #allows user to login to the program
	mail()
	print('Wnętrze login()')

def passwdChange(): #allows user to change a password (after login)
	print('Type your old password: ')
	oldPasswd = str(stdiomask.getpass())
	if oldPasswd == correctPasswd.group(1):
		print('Type your new password: ')
		newPasswd = str(stdiomask.getpass())
		if newPasswd == oldPasswd:
			print('New password can not be the same as the old password!')
			menu()
		change = open('passes.txt', 'r')
		for j in change:
			line = str(j)
			currentUserName = re.search(name, line)
			currentUserPasswd = re.search(oldPasswd, line)
			buff = open('buffor.txt', 'a')
			if currentUserName and currentUserPasswd:
				line = re.sub(oldPasswd, newPasswd, line)	
				buff.write(line)
				print('Password was successfully changed.')
			else:
				buff.write(line)
		change.close()		
		buff.close()
	os.remove('passes.txt')
	change = open('passes.txt', 'w')
	buff = open('buffor.txt', 'r')
	for i in buff:
		change.write(i)
	change.close()
	buff.close()
	os.remove('buffor.txt')
	menu()

def changePattern(): #allows to read "data.txt" and change a pattern word(s) for some other word(s)
	print('changePattern')

def addUser(): #allows to add a new user
	add = open('passes.txt', 'a')
	newUserName = input('Email: ')
	#newUserPassword = input('Password: ')
	newUserPassword = str(stdiomask.getpass())
	newUser = str(newUserName + ';' + newUserPassword + '\n')
	add.write(newUser)
	add.close() 
	print('New user was successfully added.')
	menu()

def exit(): #function that exits the program
	print('Exit')

menu()
